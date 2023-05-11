import json
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
    TextDecoration,
    Container,
    Ref,
)



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
        self.type = task_data['type']
        self.description = Ref[Container]()

    def build(self):
        if self.type == 'homework':
            task_url = f'http://courses.cuc.edu.cn/course/{self.course_id}/learning-activity#/{self.id}'
        elif self.type == 'exam':
            task_url = f"http://courses.cuc.edu.cn/course/{self.course_id}/learning-activity#/exam/{self.id}"
        brief = Row(alignment='spaceBetween',
                   controls=[
                       Column(width=300,
                              controls=[Text(spans=[TextSpan(text=self.course_name, on_enter=self.title_entered, on_exit=self.title_unentered,
                                                             style=TextStyle(), url=f'http://courses.cuc.edu.cn/course/{self.course_id}/content#')], font_family='MSYH'),],
                              ),
                       Column(width=300,
                              controls=[Text(spans=[TextSpan(text=self.title, on_enter=self.title_entered, on_exit=self.title_unentered,
                                                             style=TextStyle(), url=task_url)], font_family='MSYH'),],
                              ),
                       Column(width=150,
                              controls=[Text(value=self.end_time),],
                              ),
                        Container(content=Text(spans=[TextSpan(text="详情",
                                                    style=TextStyle(color=ft_colors.BLUE,
                                                                    decoration=TextDecoration.UNDERLINE),
                                                    on_click=self.more_clicked),
                                                    
                                                    ],font_family='MSYH',width=50))
                              
                   ],
                   )
        return Column(controls=[brief,Container(ref=self.description,
                                                visible=False,)],auto_scroll=True)
    
    def more_clicked(self, e):
        if self.description.current.visible == True:
            self.description.current.visible = False
            self.description.current.update()
        else:
            self.description.current.bgcolor = ft_colors.RED
            self.description.current.height = 100
            self.description.current.visible = True
            self.description.current.update()

    def title_entered(self, e):
        e.control.style.color = ft_colors.BLUE
        e.control.style.decoration = TextDecoration.UNDERLINE
        e.control.update()

    def title_unentered(self, e):
        e.control.style.color = None
        e.control.style.decoration = None
        e.control.update()
