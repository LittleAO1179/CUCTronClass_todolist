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
    alignment,
    Theme
)

# 登录查询程序


class login_tronclass(UserControl):
    pass

# TronToDo主程序


class TronToDo(UserControl):
    def __init__(self, page: Page):
        super().__init__()

    def build(self):
        self.cookie_input = TextField(
            label='Cookies',
            hint_text='在这里输入你的Cookies',
            on_submit=self.search_clicked,
            expand=True
        )
        self.filter = Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[Tab(text='按名称排序'), Tab(text='按时间排序')]
        )
        self.tasks = Column()
        self.item_count = Text("共有0个待办事项")

        return Column(
            width=600,
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

    def search_clicked():
        pass

    def tabs_changed():
        pass

    def clear_clicked(self):
        pass

    def update(self):
        super().update()


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
    page.update()


app(target=main)
