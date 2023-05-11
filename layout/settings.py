from flet import (
    UserControl,
    TextField,
    Page,
    app,
    Container,
    ElevatedButton,
    alignment,
    Column,
    Text,
    MainAxisAlignment,
    colors,
    AlertDialog,
    Image,
    Ref,
    ProgressRing,
    Row
)
from process.login import CookiesProcess
from time import sleep
from msedge.selenium_tools import (EdgeOptions,Edge)


class SettingsLayout(UserControl):
    def __init__(self, page:Page):
        super().__init__()
        self.page = page
        self.cookie = CookiesProcess.read_cookie()
        self.main_layout = Container(width=600,alignment=alignment.top_left)
        self.Alert = Ref[AlertDialog]()
        self.QRalert = AlertDialog(modal=True)
        self.login_progress = Ref[ProgressRing]()
        self.code_input = Ref[TextField]()
        self.cookie_input = TextField(value=self.cookie,width=600,multiline=True,on_submit=self.update_cookie)
        self.name = Ref[ElevatedButton]()

    def build(self):

        self.main_layout.content = Column(controls=[
            Text(value='保存的Cookies信息，如果Cookies有误，可以点击登录按钮更新。'),
            self.cookie_input,
            Row([
                ElevatedButton(ref=self.name,text='测试可用性',on_click=self.test_clicked),
                ElevatedButton(text='登录',on_click=self.login_clicked),
                 ProgressRing(ref=self.login_progress,visible=False)]),
        ],
        width=600,alignment=MainAxisAlignment.START)
        return self.main_layout
    
    def update_cookie(self, e):
        CookiesProcess.write_cookie(
            {'Cookie':e.value}
        )
    
    def test_clicked(self, e):
        self.login_progress.current.visible = True
        self.login_progress.current.update()
        name = CookiesProcess.get_name(CookiesProcess.get_header())
        if name != None:
            self.name.current.text = f"你好，{name}同学"
            self.name.current.bgcolor = colors.LIGHT_GREEN_50
        else:
            self.name.current.text = f"测试失败"
            self.name.current.bgcolor = colors.RED_50
        self.name.current.update()
        self.login_progress.current.visible = False
        self.login_progress.current.update()


    def login_clicked(self, e):
        self.login_progress.current.visible = True
        self.login_progress.current.update()
        options = EdgeOptions()
        options.use_chromium = True
        options.add_argument('headless')
        options.add_argument('disable-gpu')
        options.add_argument('--disable-blink-features=AutomationControlled')
        browser =Edge('msedgedriver.exe', options=options)
        browser.get("http://courses.cuc.edu.cn/user/index")
        sleep(2)
        screenshot = browser.get_screenshot_as_base64()
        sleep(1)
        self.QRalert.content = Column([Text('微信扫码并登录：'),Image(src_base64=screenshot)])
        self.page.dialog = self.QRalert
        self.QRalert.open = True
        self.page.update()
        while browser.title == '统一身份认证平台':
            sleep(1)
        def alert_close(e):
            self.QRalert.open = False
            self.page.update()
        alert_close(None)
        send_code = browser.find_element_by_xpath('//*[@id="getDynamicCode"]')
        send_code.click()
        self.QRalert.content = Column([Text('请输入手机收到的验证码：'),TextField(ref=self.code_input,on_submit=alert_close)],height=200)
        self.page.dialog = self.QRalert
        self.QRalert.open = True
        self.page.update()
        while len(self.code_input.current.value) != 6:
            pass
        code_input = browser.find_element_by_xpath('//*[@id="dynamicCode"]')
        code_input.send_keys(self.code_input.current.value)
        browser.find_element_by_xpath('//*[@id="userNameDiv"]/div[4]/button').click()
        sleep(1)
        while browser.title == '统一身份认证':
            self.QRalert.content = Column([Text('验证码错误，请尝试重新输入：'),TextField(ref=self.code_input,on_submit=alert_close,height=200)])
            self.page.dialog = self.QRalert
            self.QRalert.open = True
            self.page.update()
            while len(self.code_input.current.value) != 6:
                pass
            code_input.clear()
            code_input.send_keys(self.code_input.current.value)
            browser.find_element_by_xpath('//*[@id="userNameDiv"]/div[4]/button').click()
            sleep(1)
        cookies = browser.get_cookies()
        for i in cookies:
            if i['name'] == 'session':
                cookie = {'Cookie':f"{i['name']}={i['value']}"}
        CookiesProcess.write_cookie(cookie)
        self.cookie_input.value = CookiesProcess.read_cookie()
        self.cookie_input.update()
        self.login_progress.current.visible = False
        self.login_progress.current.update()


# def main(page : Page):
#     app = SettingsLayout()
#     page.add(app)
#     page.update()

# app(target=main)
