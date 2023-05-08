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
    Container,
    Ref
)
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.types import AnimationValue, ClipBehavior, OffsetValue, ResponsiveNumber, RotateValue, ScaleValue

class SideBar(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.settings = Ref[IconButton]()
        self.todo = Ref[IconButton]()   # 待办按钮
        self.event = Ref[IconButton]()
        self.page = page
        self.page.on_resize = self.on_resize
        self.main = Column(controls=[
            IconButton(icon=icons.DOMAIN_VERIFICATION,tooltip='动态',ref=self.event),
            Container(content=IconButton(icon=icons.DASHBOARD,tooltip='待办',ref=self.todo)),
        ],alignment=MainAxisAlignment.START,)
        self.additions = Column(controls=[
            IconButton(icon=icons.MENU,tooltip='设置',ref=self.settings),
        ],alignment=MainAxisAlignment.END)
        self.res = Column(controls=[self.main, self.additions],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    horizontal_alignment=MainAxisAlignment.CENTER,
                    height=self.page.height-20,
                    spacing=0
                    )

    def build(self):
        return self.res
    
    def on_resize(self, e):
        self.res.height = self.page.height-20
        self.res.update()

        
