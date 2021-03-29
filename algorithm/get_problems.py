from bs4 import BeautifulSoup
import pandas as pd
import requests
import os
import time

DATA_DIR = "./new_data"

# 백준에 있는 모든 문제 번호, 제목, 맞은 사람 수, 제출 수, 정답 비율 가져온다
def get_all_problem_in_baekjoon() :
    URL = 'https://www.acmicpc.net/problemset/'

    problem_ids = []
    problem_names = []
    problem_informations = []
    problem_correct_users = []
    problem_submission_cnts = []
    problem_correct_rates = []

    for page in range(1, 204) :
        problemURL = URL + str(page)
        webpage = requests.get(problemURL)
        bs = BeautifulSoup(webpage.content, "html.parser")

        problems = bs.find('div', {'class': 'table-responsive'}).find('table').find('tbody').find_all('tr')

        for problem in problems :
            problem_info = problem.find_all('td')
            # 문제번호, 문제제목, 정보, 맞은사람, 제출, 정답비율
            # print(list(map(lambda x : x.text, problem_info)))

            # 문제번호
            problem_ids.append(int(problem_info[0].text))

            # 문제제목
            problem_name = str(problem_info[1].text)
            problem_names.append(problem_name)

            # 문제정보
            information_list = list(map(lambda x : x.text, problem_info[2].find_all('span')))
            information_text = ",".join(information_list)

            problem_informations.append(information_text)

            # 문제 맞은 사람 수
            problem_correct_users.append(int(problem_info[3].text))

            # 문제 제출 수
            problem_submission_cnts.append(int(problem_info[4].text))

            # 문제 정답 비율, % 제외하고 변환
            problem_correct_rates.append(float(problem_info[5].text[:-1]))
    
    all_problem_in_baekjoon = pd.DataFrame(
            {
                'id' : problem_ids, 
                'name' : problem_names, 
                'information' : problem_informations, 
                'correct_user' : problem_correct_users, 
                'submission_cnt' : problem_submission_cnts, 
                'correct_rate' : problem_correct_rates
            })

    all_problem_in_baekjoon.to_csv(os.path.join(DATA_DIR, "all_problem_in_baekjoon.csv"), index = False, encoding='utf-8-sig')
    pd.to_pickle(all_problem_in_baekjoon, os.path.join(DATA_DIR, "all_problem_in_baekjoon.pkl"))

# 솔브드에서 문제 아이디와 난이도, 제목, 평균시도 가져오기
def get_all_problem_in_solved() :
    URL = 'https://solved.ac/problems/level/'

    problem_ids = []
    problem_levels = []
    problem_names = []
    problem_avg_trys = []

    for level in range(31) :
        last_page = 1
        problemURL = URL + str(level)
        level_page = requests.get(problemURL)
        
        # 해당 레벨의 마지막 페이지 번호 리스트 가져오기
        pages = BeautifulSoup(level_page.content, "html.parser").find('div', {'class': 'bMOKnn'}).find_all('a')

        # 페이지가 한개 이상이라면 마지막 페이지를 last_page로
        if len(pages) != 0 :
            last_page = int(pages[-1].find('div', {'class': 'kzFdWo'}).text)

        for page_num in range(1, last_page + 1) :
            page = requests.get(problemURL + "?page=" + str(page_num))
            bs = BeautifulSoup(page.content, "html.parser")

            problems = bs.find_all('div', {'class': 'cDWUBS'})

            for problem in problems[1:] :
                info = problem.find_all('div', {'class': 'fPLIhN'})

                # 문제 난이도 높을수록 어렵다
                problem_levels.append(level)

                # 문제 번호
                problem_ids.append(int(info[0].text))

                # 문제 제목
                problem_names.append(info[1].text)

                # 문제 평균 시도 횟수
                avg_try = info[-1].text.replace(',', '')
                problem_avg_trys.append(float(avg_try))

    all_problem_in_solved = pd.DataFrame(
            {
                'id' : problem_ids, 
                'name' : problem_names, 
                'level' : problem_levels,
                'avg_try' : problem_avg_trys
            })

    all_problem_in_solved.to_csv(os.path.join(DATA_DIR, "all_problem_in_solved.csv"), index = False, encoding='utf-8-sig')
    pd.to_pickle(all_problem_in_solved, os.path.join(DATA_DIR, "all_problem_in_solved.pkl"))

# 백준에서 알고리즘 목록 가져오기
def get_all_algorithm():
    URL = 'https://www.acmicpc.net/problem/tags'

    algo_id = []
    algo_url_list = []
    algo_name_kr_list = []
    algo_name_en_list = []
    algo_problem_cnt_list = []

    webpage = requests.get(URL)
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
            'algo_id' : algo_id, 
            'algo_name_kr' : algo_name_kr_list, 
            'algo_name_en' : algo_name_en_list,
            'algo_url' : algo_url_list, 
            'algo_cnt' : algo_problem_cnt_list
        })

    algorithms_df.to_csv(os.path.join(DATA_DIR, "algorithms.csv"), index = False, encoding='utf-8-sig')
    pd.to_pickle(algorithms_df, os.path.join(DATA_DIR, "algorithms.pkl"))
            
# 알고리즘별 문제 가져오기(문제 아이디, 제목, 알고리즘 분류)
def get_problem_with_algorithm():
    url = 'https://www.acmicpc.net/problemset?sort=ac_desc&algo='
    etc = '&algo_if=and&page='

    algo_name_list = []
    problem_id_list = []
    problem_name_list = []
    algo_id_list = []

    algorithm = pd.read_pickle("./new_data/algorithms.pkl")

    algo_ids = algorithm['algo_id']
    algo_names = algorithm['algo_name_kr']

    for algorithm_id, algorithm_name in zip(algo_ids, algo_names) :

        problem_webpage = requests.get(url + str(algorithm_id))
        problem_soup = BeautifulSoup(problem_webpage.content, "html.parser")

        end_page = int(problem_soup.find('ul', {'class': 'pagination'}).find_all('li')[-1].text)

        for page_num in range(1, end_page + 1) :
            detail_webpage = requests.get(url + str(algorithm_id) + etc + str(page_num))
            detail_soup = BeautifulSoup(detail_webpage.content, "html.parser")

            problem_rows = detail_soup.find('div', {'class': 'table-responsive'}).find('table').find('tbody').find_all('tr')

            for problem in problem_rows :
                tds = problem.find_all('td')

                algo_id_list.append(algorithm_id)
                algo_name_list.append(algorithm_name)

                problem_id_list.append(int(tds[0].text))
                problem_name_list.append(tds[1].text)
    
    problem_infos_df = pd.DataFrame(
        {
            'id' : problem_id_list,
            'name' : problem_name_list,
            'algo' : algo_name_list, 
            'algo_id' : algo_id_list
        })

    problem_infos_df.to_csv(os.path.join(DATA_DIR, "all_problem_with_algorithm.csv"), index = False, encoding='utf-8-sig')
    pd.to_pickle(problem_infos_df, os.path.join(DATA_DIR, "all_problem_with_algorithm.pkl"))

def get_recommend_problem_with_datail_information():
    url = "https://www.acmicpc.net/problem/"
    recommend_problem_numbers = pd.read_pickle("./new_data/recommend_problems.pkl")['id']
    
    numbers = []
    time_limits = []
    memory_limits = []
    submission_cnts = []
    answer_cnts = []
    correct_user_cnts = []
    answer_rates = []

    for number in recommend_problem_numbers:
        problem_page = requests.get(url + str(number))
        problem_soup = BeautifulSoup(problem_page.content, "html.parser")

        row = problem_soup.find('div', {'class': 'table-responsive'}).find('table').find('tbody').find('tr').find_all('td')

        infos = [a.text for a in row]

        numbers.append(number)
        time_limits.append(infos[0].rstrip())
        memory_limits.append(infos[1])
        submission_cnts.append(infos[2])
        answer_cnts.append(infos[3])
        correct_user_cnts.append(infos[4])
        answer_rates.append(infos[5])

    problem_detail_infos_df = pd.DataFrame(
        {
            'number' : numbers,
            'time_limit' : time_limits,
            'memory_limit' : memory_limits, 
            'submission_cnt' : submission_cnts,
            'answer_cnt' : answer_cnts,
            'correct_user_cnt' : correct_user_cnts,
            'answer_rate' : answer_rates,
        })

    problem_detail_infos_df.to_csv(os.path.join(DATA_DIR, "recommend_problem_with_datail_information.csv"), index = False, encoding='utf-8-sig')
    pd.to_pickle(problem_detail_infos_df, os.path.join(DATA_DIR, "recommend_problem_with_datail_information.pkl"))


def main():
    # get_all_problem_in_baekjoon()
    # get_all_problem_in_solved()
    # get_all_algorithm()
    # get_problem_with_algorithm()
    get_recommend_problem_with_datail_information()

if __name__ == "__main__":
    main()