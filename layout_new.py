import json
from login import LoginTronClass
from flet import (
    Page,
    app,
    Text,
    TextField,
    UserControl,
    Tabs,
    Tab,
    Column,
    Row,
    OutlinedButton,
    icons,
    Theme,
    SnackBar,
    TextSpan,
    colors as ft_colors,
    TextStyle,
    TextDecoration
)

# 登录查询程序


class Task(UserControl):
    def __init__(self, task_data: dict):
        '''
        `task_data`: 传入课程的字典
        '''
        super().__init__()
        self.course_name = task_data['course_name']
        self.end_time = task_data['end_time']
        self.type = task_data['type']
        self.title = task_data['title']
        self.id = task_data['id']
        self.course_id = task_data['course_id']

    def build(self):
        return Row(alignment='spaceBetween',
                   controls=[
                       Column(width=300,
                              controls=[Text(spans=[TextSpan(text=self.course_name, on_enter=self.title_entered, on_exit=self.title_unentered,
                                                             style=TextStyle(), url=f'http://courses.cuc.edu.cn/course/{self.course_id}/content#')], font_family='MSYH'),],
                              ),
                       Column(width=300,
                              controls=[Text(spans=[TextSpan(text=self.title, on_enter=self.title_entered, on_exit=self.title_unentered,
                                                             style=TextStyle(), url=f'http://courses.cuc.edu.cn/course/{self.course_id}/learning-activity#/{self.id}')], font_family='MSYH'),],
                              ),
                       Column(width=200,
                              controls=[Text(value=self.end_time),],
                              ),
                   ],
                   )

    def title_entered(self, e):
        e.control.style.color = ft_colors.BLUE
        e.control.style.decoration = TextDecoration.UNDERLINE
        e.control.update()

    def title_unentered(self, e):
        e.control.style.color = None
        e.control.style.decoration = None
        e.control.update()


class TronToDo(UserControl):
    def __init__(self, page: Page):
        self.count = 0
        self.cookies = ''
        self.task_inf = ''
        self.page = page
        super().__init__()

    def build(self):
        self.cookies = self.auto_read_cookies()
        self.cookie_input = TextField(
            label='Cookies',
            hint_text='在这里输入你的Cookies',
            on_submit=self.search_clicked,
            expand=True,
            value=self.cookies
        )
        self.filter = Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[Tab(text='按名称排序'), Tab(text='按时间排序')]
        )
        self.tasks = Column(scroll='ADAPTIVE')
        self.item_count = Text(f"共有{self.count}个待办事项")

        return Column(
            width=800,
            # TODO: 改字体
            controls=[
                Row([Text(value='畅课代办查询', style="headlineMedium", font_family='MSYH'), ],
                    alignment='center', height=90,),
                Row(
                    controls=[
                        self.cookie_input,
                        OutlinedButton(
                            icon=icons.SEARCH,
                            on_click=self.search_clicked
                        )
                    ],
                ),
                Column(
                    spacing=25,
                    controls=[
                        self.filter,
                        Row(alignment='spaceBetween',
                            controls=[
                                Column(width=300,
                                       controls=[
                                           Text(value='课程名称'),],
                                       ),
                                Column(width=300,
                                       controls=[
                                           Text(spans=[TextSpan(text='标题')], font_family='MSYH'),],
                                       ),
                                Column(width=200,
                                       controls=[Text(value='截止时间'),],
                                       ),
                            ],
                            ),
                        self.tasks,
                        Row(
                            alignment="spaceBetween",
                            vertical_alignment="CENTER",
                            controls=[
                                self.item_count,
                                OutlinedButton(
                                    text="清除数据", on_click=self.clear_clicked
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )

    # 按下搜索按键
    def search_clicked(self, e):
        self.tasks.clean()
        self.count = 0
        if self.header['Cookie'] != self.cookie_input.value:
            self.auto_write_cookies()
            self.header['Cookie'] = self.cookie_input.value
        self.auto_read_cookies()
        login_func = LoginTronClass(self.header)
        self.task_inf = login_func.login_attempt()
        if self.task_inf == -1:
            self.login_error()
            self.update()
            return
        self.tabs_changed(e=None)
        self.update()

    def login_error(self):
        self.send_error("发生错误，可能是没有设置好Cookies，请正确设置Cookies")

    def send_error(self, message: str):
        self.page.snack_bar = SnackBar(content=Text(
            value=message))
        self.page.snack_bar.open = True
        self.page.update()

    def tabs_changed(self, e):
        self.tasks.clean()
        self.count = 0
        self.item_count.value = f"共有{self.count}个待办事项"
        status = self.filter.tabs[self.filter.selected_index].text
        if status == '按名称排序':
            sorted_tasks = sorted(self.task_inf, key= lambda x: x['course_name'])
            for i in sorted_tasks:
                task = Task(i)
                self.tasks.controls.append(task)
                self.count += 1
        else:
            sorted_tasks = sorted(self.task_inf, key= lambda x: x['end_time'])
            for i in sorted_tasks:
                task = Task(i)
                self.tasks.controls.append(task)
                self.count += 1
        self.update()

    def clear_clicked(self, e):
        self.tasks.clean()
        self.count = 0
        self.item_count.value = f"共有{self.count}个待办事项"
        self.cookie_input.value = ''
        self.update()

    def update(self):
        self.item_count.value = f"共有{self.count}个待办事项"
        super().update()

    def auto_read_cookies(self):
        if self.cookies == '':
            with open('headers.json') as user_file:
                header_str = user_file.read()
                self.header = json.loads(header_str)
            if self.header['Cookie'] != '':
                return self.header['Cookie']
        return ''

    def auto_write_cookies(self):
        if self.cookie_input.value != '':
            header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64",
                "Cookie": ""
            }
            header["Cookie"] = self.cookie_input.value
            with open('headers.json', 'w') as user_file:
                user_file.write(json.dumps(
                    header, indent=4, ensure_ascii=False))
        self.auto_read_cookies()
# 测试用代码


def main(page: Page):
    app = TronToDo(page)
    page.add(app)
    page.title = 'TronClass代办查询'
    page.horizontal_alignment = "CENTER"
    page.fonts = {
        "MSYH": "fonts\MSYH.TTC"
    }
    page.theme = Theme(font_family='MSYH')
    page.theme_mode = 'light'
    page.scroll = "adaptive"
    page.update()


app(target=main)
