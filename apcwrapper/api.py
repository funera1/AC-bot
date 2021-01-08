import json
from collections import Counter
from pprint import pprint

import requests


def get_submissions(user) -> list[dict]:
    "{'id': 8096604, 'epoch_second': 1571828266, 'problem_id': 'abc143_b', 'contest_id': 'abc143', 'user_id': 't4t5u0', 'language': 'Python3 (3.4.3)', 'point': 200.0, 'length': 154, 'result': 'AC', 'execution_time': 18}"
    # user = 't4t5u0'
    url = f'https://kenkoooo.com/atcoder/atcoder-api/results?user={user}'
    res = requests.get(url)
    # print(res.text)
    return json.loads(res.text)


def get_ac_languages(user):
    """
    {
        'user_id': 't4t5u0',   
        'languages':  
            [
                {'language': 'Python', 'count': 103},  
                {'language': 'Julia', 'count': 1}
            ] 
    }
    """
    sub = get_submissions(user)
    problem_ids = []
    languages = [item["language"]
                 for item in sub
                 if item['result'] == 'AC'
                # 一時変数に束縛
                 and (x := (item['problem_id'], item['language']))
                # problem_idsが重複していなかったら
                 and x not in problem_ids
                # (problem_id, language) を problem_ids に追加
                 and not problem_ids.append(x)]
    result = {
        'user_id': user,
        'languages': [
            {'language': item[0], 'count':item[1]}
            for item in Counter(languages).most_common()
        ]
    }
    return result



if __name__ == "__main__":
    # get_languages()
    # get_submissions()
    pprint(get_ac_languages('t4t5u0'))
