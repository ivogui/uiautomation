from zikaow.Page.basepage import BasePage


class Login(BasePage):

    def login(self):
        self.steps('D:\\zikaow\\zikaow\\TestData\\login.yml', 'login')

    def loginByPassword(self, account, password):
        self.steps('D:\\zikaow\\zikaow\\TestData\\login.yml', 'loginByPassword', var1=account, var2=password)