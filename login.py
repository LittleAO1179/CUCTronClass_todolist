import requests
import json


def read_headers():
    with open('headers.json') as user_file:
        header_str = user_file.read()
        header = json.loads(header_str)
    return header


def login():
    header = read_headers()
    r = requests.get(
        'http://courses.cuc.edu.cn/api/todos?no-intercept=true', headers=header)

    # Cookies设置错误
    try:
        res = [i for i in r.json()['todo_list']]
    except:
        print('发生错误，可能是没有设置好Cookies，请在headers.json中正确设置Cookies')
        exit(0)

    return res
