import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 알고리즘 분류 가져오기
def make_type_dict() :
    type_dict = pd.read_pickle(os.path.join(BASE_DIR, 'static', 'data', 'type.pkl'))
    type_dict = dict(zip(type_dict['id'], type_dict['name']))
    
    return type_dict

# 문제별 알고리즘 분류 가져오기
def make_problem_type_dict() :
    p2t = pd.read_pickle(os.path.join(BASE_DIR, 'static', 'data', 'problem2type.pkl'))
    p2t = dict(zip(p2t['number'], p2t['algorithm_id']))
    
    return p2t

# 문제난이도별 경험치 가져오기
def make_problem_exp_dict() :
    problem_exps = pd.read_pickle(os.path.join(BASE_DIR, 'static', 'data', 'problem_exps.pkl'))
    problem_exps = dict(zip(problem_exps['number'], problem_exps['exp']))
    
    return problem_exps

# 레벨별 필요 경험치 가져오기
def make_level_exp_dict() :
    level_exps = pd.read_pickle(os.path.join(BASE_DIR, 'static', 'data', 'level_exps.pkl'))
    level_exps = dict(zip(level_exps['level'], level_exps['exp']))
    
    return level_exps