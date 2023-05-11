import json
from typing import Any, List, Optional, Union
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
    MainAxisAlignment,
    Container,
    ResponsiveRow,
    alignment,
    IconButton
)
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.types import AnimationValue, ClipBehavior, OffsetValue, ResponsiveNumber, RotateValue, ScaleValue
from process.login import LoginTronClass
from layout.layout_sidebar import SideBar
from layout.layout import TronToDo
from layout.settings import SettingsLayout

class MainLayout(UserControl):
    def __init__(self, page : Page):
        super().__init__()
        self.page = page
        self.sidebar = SideBar(self.page)
        self.layout_todo = TronToDo(self.page)
        self.settings = SettingsLayout(self.page)
        self.page.on_resize = self.on_resize
        self.layout_sidebar = Container(self.sidebar,bgcolor=ft_colors.BLACK12)
        self.main_content = Container(content=self.layout_todo,
                                    width=self.page.width,
                                    alignment=alignment.top_center,
                                    height=self.page.height-50)
        self.res = Row(controls=[self.layout_sidebar,self.main_content,])


    def build(self):
        self.sidebar.settings.current.on_click = self.settings_clicked
        self.sidebar.todo.current.on_click = self.todo_clicked
        self.sidebar.event.current.on_click = self.event_clicked
        return self.res
    
    def on_resize(self, e):
        self.main_content.width = self.page.width
        self.main_content.alignment = alignment.top_center
        self.main_content.height = self.page.height - 50
        self.main_content.update()

    def settings_clicked(self ,e):
        self.main_content.content = self.settings
        self.main_content.update()
        self.page.update()

    def todo_clicked(self, e):
        self.main_content.content = self.layout_todo
        self.main_content.update()

    def event_clicked(self, e):
        self.main_content.content = Text("此页面建设中，敬请期待。")
        self.main_content.update()