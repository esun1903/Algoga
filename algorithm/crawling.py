from bs4 import BeautifulSoup
import pandas as pd
import requests
import os
import time

DATA_DIR = "./data"

RANKER_FILE = os.path.join(DATA_DIR, "rankers.csv")
RANKER_PKL = os.path.join(DATA_DIR, "rankers.pkl")

RANKER_PROBLEMS_FILE = os.path.join(DATA_DIR, "ranker_problems.csv")
RANKER_PROBLEMS_PKL = os.path.join(DATA_DIR, "ranker_problems.pkl")

PROBLEM_FILE = os.path.join(DATA_DIR, "problems.csv")
PROBLEM_PKL = os.path.join(DATA_DIR, "problems.pkl")

PROBLEM_INFOS_FILE = os.path.join(DATA_DIR, "problem_infos.csv")
PROBLEM_INFOS_PKL = os.path.join(DATA_DIR, "problem_infos.pkl")

ALGORITHM_FILE = os.path.join(DATA_DIR, "algorithms.csv")
ALGORITHM_PKL = os.path.join(DATA_DIR, "algorithms.pkl")

rankpage = "https://www.acmicpc.net/ranklist/"
userpage = "https://www.acmicpc.net/user/"
problempage = "https://solved.ac/problems/level/"  # https://solved.ac/problems/level/0 ~ 30?page=1

# 백준 문제와 문제 난이도 가져오기
def get_all_problem() :
    problem_level_list = []
    problem_number_list = []
    problem_name_list = []

    for level in range(31) :
        last_page = 1
        problemURL = problempage + str(level)
        webpage = requests.get(problemURL)
        bs = BeautifulSoup(webpage.content, "html.parser")

        pages = bs.find('div', {'class': 'bMOKnn'}).find_all('a')

        if len(pages) != 0 :
            last_page = int(pages[-1].find('div', {'class': 'kzFdWo'}).text)

        for page_num in range(1, last_page + 1) :
            webpage = requests.get(problemURL + "?page=" + str(page_num))
            bs = BeautifulSoup(webpage.content, "html.parser")

            problems = bs.find_all('div', {'class': 'cDWUBS'})

            for problem in problems[1:] :
                info = problem.find_all('div', {'class': 'fPLIhN'})

                problem_level_list.append(level)
                problem_number_list.append(info[0].text)
                problem_name_list.append(info[1].text)

    problems_df = pd.DataFrame({'id' : list(range(len(problem_level_list))), 'level' : problem_level_list, 'problem_id' : problem_number_list, 'name' : problem_name_list})
    problems_df.to_csv(PROBLEM_FILE, index = False, encoding='utf-8-sig')
    pd.to_pickle(problems_df, PROBLEM_PKL)
    
# 내가 푼 문제와 내 레벨 가져오기, [0] : 맞은 문제 / [-1] : 시도했지만 틀린 문제
def get_my_problems(id) :
    userURL = userpage + id
    webpage = requests.get(userURL)
    bs = BeautifulSoup(webpage.content, "html.parser")

    level = bs.find('div', {'class': 'page-header'}).h1.img
    if level is None :
        level = 999
    else :
        level = level['src'].split('/')[-1].split('.')[0]

    divs = bs.findAll('div', {'class': 'panel-body'})

    
    user_problems = []
    for div in divs :
        problems = list(map(lambda x : x.text, div.find_all('a')))
        user_problems.append(problems)
    
    return level, user_problems

# 문제를 추천하기 위해 랭커 아이디 가져오기(문제 푼 수로 컷)
def get_rankers_solved_cnt() :
    user_id_list = []
    user_correct_problem_list = []

    # 맞은 문제가 100문제 이상일떄까지 검색
    page_num, end_condition = 1, 100

    while True :
        webpage = requests.get(rankpage + str(page_num))
        soup = BeautifulSoup(webpage.content, "html.parser")
        rows = soup.find('div', {'class': 'table-responsive'}).find('table').find('tbody').find_all('tr')

        for row in rows :
            info = row.find_all('td')

            user_id = info[1].find('a').text
            correct_cnt = info[3].find('a').text

            user_id_list.append(user_id)
            user_correct_problem_list.append(correct_cnt)
        
        if int(user_correct_problem_list[-1]) < end_condition :
            break
        
        page_num += 1
    
    if len(user_id_list) != len(user_correct_problem_list) :
        print("데이터 추출 중 에러 발생")
        return
    
    rankers_df = pd.DataFrame({'id' : user_id_list, 'correct_cnt' : user_correct_problem_list})
    rankers_df.to_csv(RANKER_FILE, index = False)

# 문제를 추천하기 위해 랭커 아이디 가져오기(페이지로 가져오기)
def get_rankers_page():
    user_id_list = []
    user_correct_problem_list = []

    for page_num in range(1, 350) :
        webpage = requests.get(rankpage + str(page_num))
        soup = BeautifulSoup(webpage.content, "html.parser")
        rows = soup.find('div', {'class': 'table-responsive'}).find('table').find('tbody').find_all('tr')

        for row in rows :
            info = row.find_all('td')

            user_id = info[1].find('a').text
            correct_cnt = info[3].find('a').text

            user_id_list.append(user_id)
            user_correct_problem_list.append(correct_cnt)
    
    if len(user_id_list) != len(user_correct_problem_list) :
        print("데이터 추출 중 에러 발생")
        return
    
    rankers_df = pd.DataFrame({'id' : list(range(len(user_id_list))), 'user' : user_id_list, 'correct_cnt' : user_correct_problem_list})
    rankers_df.to_csv(RANKER_FILE, index = False)
    pd.to_pickle(rankers_df, RANKER_PKL)

# 알고리즘 분류 목록 가져오기
def get_algorithm_info():

    algo_id = []
    algo_url_list = []
    algo_name_kr_list = []
    algo_name_en_list = []
    algo_problem_cnt_list = []

    webpage = requests.get('https://www.acmicpc.net/problem/tags')
    soup = BeautifulSoup(webpage.content, "html.parser")
    rows = soup.find('div', {'class': 'table-responsive'}).find('table').find('tbody').find_all('tr')

    for row in rows :
        infos = row.find_all('td')

        algo_name_kr_list.append(infos[0].text)
        algo_url_list.append(infos[0].a['href'])
        algo_id.append(infos[0].a['href'].split('/')[-1])

        algo_name_en_list.append(infos[1].text)
        algo_problem_cnt_list.append(infos[2].text)

    algorithms_df = pd.DataFrame(
        {
            'id' : list(range(len(algo_name_kr_list))), 
            'algo_id' : algo_id, 
            'algo_name_kr' : algo_name_kr_list, 
            'algo_name_en' : algo_name_en_list,
            'algo_url' : algo_url_list, 
            'algo_cnt' : algo_problem_cnt_list
        })

    algorithms_df.to_csv(ALGORITHM_FILE, index = False, encoding='utf-8-sig')
    pd.to_pickle(algorithms_df, ALGORITHM_PKL)
            
# 문제별 정보 가져오기(제출, 맞은 사람, 정답 비율, 알고리즘 분류)
def get_problem_info():
    url = 'https://www.acmicpc.net/problemset?sort=ac_desc&algo='
    etc = '&algo_if=and&page='

    algo_name_list = []
    problem_id_list = []
    problem_name_list = []
    problem_correct_people_list = []
    problem_submission_list = []
    problem_correct_rate = []

    webpage = requests.get('https://www.acmicpc.net/problem/tags')
    soup = BeautifulSoup(webpage.content, "html.parser")
    algo_rows = soup.find('div', {'class': 'table-responsive'}).find('table').find('tbody').find_all('tr')

    for algo_row in algo_rows :
        algo_infos = algo_row.find_all('td')

        algo_name = algo_infos[0].text
        algo_id = algo_infos[0].a['href'].split('/')[-1]

        problem_webpage = requests.get(url + str(algo_id))
        problem_soup = BeautifulSoup(problem_webpage.content, "html.parser")

        end_page = int(problem_soup.find('ul', {'class': 'pagination'}).find_all('li')[-1].text)

        for page_num in range(1, end_page + 1) :
            detail_webpage = requests.get(url + str(algo_id) + etc + str(page_num))
            detail_soup = BeautifulSoup(detail_webpage.content, "html.parser")

            problem_rows = detail_soup.find('div', {'class': 'table-responsive'}).find('table').find('tbody').find_all('tr')

            for problem in problem_rows :
                tds = problem.find_all('td')

                algo_name_list.append(algo_name)
                problem_id_list.append(tds[0].text)
                problem_name_list.append(tds[1].text)
                problem_correct_people_list.append(tds[3].text)
                problem_submission_list.append(tds[4].text)
                problem_correct_rate.append(tds[5].text)
    
    problem_infos_df = pd.DataFrame(
        {
            'id' : list(range(len(algo_name_list))), 
            'algo_name' : algo_name_list, 
            'problem_id' : problem_id_list,
            'problem_name' : problem_name_list, 
            'problem_correct_people_cnt' : problem_correct_people_list,
            'problem_submission' : problem_submission_list,
            'problem_correct_rate' : problem_correct_rate
        })

    problem_infos_df.to_csv(PROBLEM_INFOS_FILE, index = False, encoding='utf-8-sig')
    pd.to_pickle(problem_infos_df, PROBLEM_INFOS_PKL)

def read_pkl(PATH):
    return pd.read_pickle(PATH)

def read_csv(PATH) :
    return pd.read_csv(PATH)

def make_problem_detail():
    problems = read_pkl(PROBLEM_PKL)
    problem_infos = read_pkl(PROBLEM_INFOS_PKL)

    print(problems.dtypes)
    print(problem_infos.dtypes)

# 랭커들이 푼 문제
def get_problems_per_ranker() :
    rankers = read_pkl("./data/rankers_old.pkl")

    total = 0
    last = len(rankers['id'])
    cur = time.time()

    user_level_list = [] # 랭커 레벨

    id_list = []
    user_id_list = []
    problems_list = []
    problems_OX_list = [] # 맞았는지 틀렸는지

    os = ['o']
    xs = ['x']

    for id, user_id in zip(rankers['id'], rankers['user']) :
        level, user_problems = get_my_problems(user_id)
        user_level_list.append(level)

        problems_list += user_problems[0]
        problems_OX_list += os * len(user_problems[0])
        
        problems_list += user_problems[-1]
        problems_OX_list += xs * len(user_problems[-1])

        id_list += [id] * (len(user_problems[0]) + len(user_problems[-1]))
        user_id_list += [user_id] * (len(user_problems[0]) + len(user_problems[-1]))

        total += 1
        if(total % 100 == 0) :
            print(total / last * 100, "%, ", time.time() - cur, '초 소요....')
            cur = time.time()

    ranker_problems_df = pd.DataFrame(
        {
            'id' : list(range(len(id_list))), 
            'user_id' : id_list, 
            'user' : user_id_list, 
            'problem_id' : problems_list,
            'TF' : problems_OX_list
        })

    ranker_problems_df.to_csv(RANKER_PROBLEMS_FILE, index = False, encoding='utf-8-sig')
    pd.to_pickle(ranker_problems_df, RANKER_PROBLEMS_PKL)

    rankers['level'] = user_level_list
    rankers.to_csv(RANKER_FILE, index = False)
    pd.to_pickle(rankers, RANKER_PKL)

def main():
    # get_my_problems('kkwinwin95')
    # get_rankers_solved_cnt()
    # get_rankers_page()
    # get_all_problem()
    # get_algorithm_info()

    # make_problem_detail()
    get_problems_per_ranker()

if __name__ == "__main__":
    main()