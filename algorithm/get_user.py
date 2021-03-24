from bs4 import BeautifulSoup
import pandas as pd
import requests
import os
import time

DATA_DIR = "./data"

rankpage = "https://www.acmicpc.net/ranklist/"
userpage = "https://www.acmicpc.net/user/"
    
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
    
    rankers_df = pd.DataFrame(
        {
            'id' : list(range(len(user_id_list))), 
            'user' : user_id_list, 
            'correct_cnt' : user_correct_problem_list
        })
    rankers_df.to_csv(os.path.join(DATA_DIR, "rankers.csv"), index = False)
    pd.to_pickle(rankers_df, os.path.join(DATA_DIR, "rankers.pkl"))

# 랭커들이 푼 문제들(맞은 문제/틀린 문제)
def get_problems_per_ranker() :
    rankers = read_pkl("./data/rankers.pkl")

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

    ranker_problems_df.to_csv(os.path.join(DATA_DIR, "ranker_problems.csv"), index = False, encoding='utf-8-sig')
    pd.to_pickle(ranker_problems_df, os.path.join(DATA_DIR, "ranker_problems.pkl"))

    rankers['level'] = user_level_list
    rankers.to_csv(os.path.join(DATA_DIR, "rankers.csv"), index = False)
    pd.to_pickle(rankers, os.path.join(DATA_DIR, "rankers.pkl"))

def main():
    # get_problems_per_ranker()

if __name__ == "__main__":
    main()