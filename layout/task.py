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
    TextDecoration
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
