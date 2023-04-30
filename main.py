import requests
import json
header = {}
with open('headers.json') as user_file:
    header_str = user_file.read()
header = json.loads(header_str)

r = requests.get(
    'http://courses.cuc.edu.cn/api/todos?no-intercept=true', headers=header)

# Cookies设置错误
try:
    res = [i for i in r.json()['todo_list']]
except:
    print('发生错误，可能是没有设置好Cookies，请在headers.json中正确设置Cookies')
    exit(0)


for i in res:
    i['course_name'] = str(i['course_name']).split('-')[1]
    i['course_name'] = str(i['course_name']).split('[')[0]
    i['end_time'] = f"{str(i['end_time']).split('T')[0]} {str(i['end_time']).split('T')[1]}"
    i['end_time'] = str(i['end_time']).split('Z')[0]
    print(i['course_name'])
    print(i['end_time'])
