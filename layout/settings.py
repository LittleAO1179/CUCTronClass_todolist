from flet import (
    UserControl,
    TextField,
    Page,
    app
)
from process.login import CookiesProcess

class SettingsLayout(UserControl):
    def __init__(self):
        super().__init__()
        self.cookie = CookiesProcess.read_cookie()

    def build(self):
        self.cookie_input = TextField(value=self.cookie,width=10)
        return self.cookie_input
    


# def main(page : Page):
#     app = SettingsLayout()
#     page.add(app)
#     page.update()

# app(target=main)
