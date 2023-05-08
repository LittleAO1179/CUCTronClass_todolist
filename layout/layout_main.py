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
)
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.types import AnimationValue, ClipBehavior, OffsetValue, ResponsiveNumber, RotateValue, ScaleValue
from process.login import LoginTronClass
from layout.layout_sidebar import SideBar
from layout.layout import TronToDo


class MainLayout(UserControl):
    def __init__(self, page : Page):
        super().__init__()
        self.page = page

    def build(self):
        self.page.on_resize = self.on_resize
        self.layout_todo = TronToDo(self.page)
        self.layout_sidebar = Container(SideBar(self.page),bgcolor=ft_colors.BLACK12)
        self.main_content = Container(content=self.layout_todo,
                                      width=self.page.width,
                                    alignment=alignment.top_center,
                                    height=self.page.height-50)
        res = Row(controls=[self.layout_sidebar,self.main_content,])
        return res
    
    def on_resize(self, e):
        self.main_content.width = self.page.width
        self.main_content.alignment = alignment.top_center
        self.main_content.height = self.page.height - 50
        self.main_content.update()