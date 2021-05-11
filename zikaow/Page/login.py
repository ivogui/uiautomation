from time import sleep
from zikaow.Page.basepage import BasePage

element1 = "登录 / 注册"


class Login(BasePage):

    def oneclicklogin(self):  # 一键登录操作
        # if self.isElementPresent("xpath", "//*[contains(@text,'登录 / 注册')]") is True:
        if self.findItem(element1) is True:
            self.steps('../TestData/login.yml', 'oneclicklogin')
        else:
            self.logout()
            return self.oneclicklogin()

    def loginByPassword(self, account, password):  # 账号密码登录
        # if self.isElementPresent("xpath", "//*[contains(@text,'登录 / 注册')]") is True:
        if self.findItem(element1) is True:
            self.steps('../TestData/login.yml', 'loginByPassword', var1=account, var2=password)
        else:
            self.logout()
            return self.loginByPassword(account, password)

    def login_SMS(self, account, password):  # 验证码登录，还需要进一步扩展获取短信验证码文本，并填入输入框内
        # if self.isElementPresent("xpath", "//*[contains(@text,'登录 / 注册')]") is True:
        if self.findItem(element1) is True:
            self.steps('../TestData/login.yml', 'login_SMS', var1=account, var2=password)
        else:
            self.logout()
            return self.login_SMS(account, password)
        # sleep(2)
        # # 打开通知栏
        # self._driver.open_notifications()
        # # 获取定位短信内容
        # message = self.find("xpath", "//*[contains(@text, '')]")
        # message_content = message.text
        # ver_code = re.findall(r'[\d]{6}', message_content)
        # # 关闭通知栏
        # self._driver.press_keycode(4)
        # # 自动填入验证码
        # self.input_verification_code(ver_code)

    def logout(self):  # 退出登录操作
        self.steps('../TestData/login.yml', 'logout')
        sleep(1)

    def back(self):  # 返回操作
        self.steps('../TestData/login.yml', 'back')
