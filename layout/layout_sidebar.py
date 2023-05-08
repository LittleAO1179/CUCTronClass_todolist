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
    IconButton,
    MainAxisAlignment,
    Container
)
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.types import AnimationValue, ClipBehavior, OffsetValue, ResponsiveNumber, RotateValue, ScaleValue



class SideBar(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page

    def build(self):
        self.page.on_resize = self.on_resize
        self.main = Column(controls=[
            IconButton(icon=icons.DOMAIN_VERIFICATION,tooltip='动态'),
            Container(content=IconButton(icon=icons.DASHBOARD,tooltip='待办')),
        ],alignment=MainAxisAlignment.START,)
        self.additions = Column(controls=[
            IconButton(icon=icons.MENU,tooltip='设置'),
        ],alignment=MainAxisAlignment.END)
        self.res = Column(controls=[self.main, self.additions],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    horizontal_alignment=MainAxisAlignment.CENTER,
                    height=self.page.height-20,
                    spacing=0
                    )
        return self.res
    
    def on_resize(self, e):
        self.res.height = self.page.height-20
        self.res.update()