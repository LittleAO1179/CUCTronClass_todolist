from DrissionPage.easy_set import set_headless
from DrissionPage import WebPage

# 设置无头模式
set_headless(true)

# 启动浏览器
page = WebPage()

# 打开网页
page.change_mode()
cookie = {
    "_ga": "GA1.3.872730121.1673351573",
    "session": "V2-1000000000-76466777-2811-4b69-b445-32a276bebddc.MzY4ODQzMA.1694832819792.ukRJtszcnDXoP6CR4GI0cVxCAzI",
    "core.data.console.session": "eyJfZnJlc2giOmZhbHNlLCJfcGVybWFuZW50Ijp0cnVlfQ.ZQPHog.2HP38AsTrY9SUDaNT1hMxAGpstg"
}

page.set.cookies(cookie)
page.get('http://courses.cuc.edu.cn/api/todos?no-intercept=true')

todo = page.json['todo_list'][0]
course_id = todo['course_id']
print(todo['course_name'])

page.get(f'http://courses.cuc.edu.cn/api/courses/{course_id}/activities')

uploads = page.json['activities'][0]['uploads']

id = uploads[0]['reference_id']

page.get(
    f'http://courses.cuc.edu.cn/api/uploads/reference/document/{id}/url?preview=true')

page.download(page.json['url'])
