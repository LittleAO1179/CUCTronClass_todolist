import process.login as login

if __name__ == '__main__':
    while True:
        print('欢迎使用TronClass代办查询，这是黑窗预览版')
        if name:=login.CookiesProcess.get_name(login.CookiesProcess.read_cookie()) == None:
            print('登录失败，请重新检查你的Cookies，黑窗预览不支持登录功能，请您手动修改。')
            break
        else:
            print(f'欢迎{name}，你的Cookies已经成功设置。')
        print('请输入你想要的操作：')
