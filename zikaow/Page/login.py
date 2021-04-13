from selenium.webdriver.common.by import By
from zikaow.Page.basepage import BasePage


class Login(BasePage):

    def oneclicklogin(self):
        self.steps('D:/gitfile/uiautomation/zikaow/'
                   'TestData/login.yml', 'oneclicklogin')

    def loginByPassword(self, account, password):
        self.steps('D:/gitfile/uiautomation/zikaow/'
                   'TestData/login.yml', 'loginByPassword', var1=account, var2=password)

    def logout(self):
        self.steps('D:/gitfile/uiautomation/zikaow/'
                   'TestData/login.yml', 'logout')

    def getErrorMsg(self):

        self.toastText("登陆失败，账号或密码错误")

    def back(self):
        self.steps('D:/gitfile/uiautomation/zikaow/'
                   'TestData/login.yml', 'back')





