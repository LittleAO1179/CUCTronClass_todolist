import requests
import json
from selenium import webdriver
class LoginTronClass:
    '''
    处理畅课登录
    '''
    def __init__(self,  header: dict):
        '''
        `header`: 传入的header, header应该包括User_Agent和Cookie参数。
        '''
        self.header = header
        self.url = "http://courses.cuc.edu.cn/api/todos?no-intercept=true"

    def login_attempt(self):
        '''首次尝试用Cookie登录，若登陆成功，则会返回待办的list，登陆失败则返回`-1`,连接失败返回`-2`'''
        try: 
            data = requests.get(url=self.url, headers=self.header)
        except:
            return -2
        try:
            res = [i for i in data.json()['todo_list']]
        except:
            print('发生错误，可能是没有设置好Cookies，请正确设置Cookies')
            return -1
        return self.string_process(data.json()['todo_list'])

    def string_process(self, tmp: list):
        res = []
        for i in tmp:
            i['course_name'] = str(i['course_name']).split(
                '-')[1].split('[')[0]
            i['end_time'] = str(i['end_time']).split(
                'T')[0] + ' ' + str(i['end_time']).split('T')[1].split('Z')[0]
            res.append(i)
        return res
    
    def selenium_login(self):
        webdriver.Edge()

class CookiesProcess():
    def __init__(self):
        pass

    def read_cookie():
        with open('headers.json') as user_file:
            header_str = user_file.read()
            header = json.loads(header_str)
        return header['Cookie']