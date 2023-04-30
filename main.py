import requests
import json
header = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64',
}
Cookies = input('请输入Cookies:')

header[Cookies.split(": ")[0]] = Cookies.split(": ")[1]

r = requests.get(
    'http://courses.cuc.edu.cn/api/todos?no-intercept=true', headers=header)

res = [i for i in r.json()['todo_list']]

for i in res:
    i['course_name'] = str(i['course_name']).split('-')[1]
    i['course_name'] = str(i['course_name']).split('[')[0]
    i['end_time'] = f"{str(i['end_time']).split('T')[0]} {str(i['end_time']).split('T')[1]}"
    i['end_time'] = str(i['end_time']).split('Z')[0]
    print(i['course_name'])
    print(i['end_time'])
