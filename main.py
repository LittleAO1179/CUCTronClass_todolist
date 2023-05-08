from flet import (Page, Theme, app)
from layout.layout_main import MainLayout

def main(page: Page):
    app = MainLayout(page)
    page.add(app)
    page.title = 'TronClass代办查询'
    page.fonts = {
        "MSYH": "fonts\MSYH.TTC"
    }
    page.theme = Theme(font_family='MSYH')
    page.theme_mode = 'light'
    page.scroll = "adaptive"
    page.update()

app(target=main)