from zikaow.Page.basepage import BasePage


class Login(BasePage):

    def oneclicklogin(self):
        self.steps('/Users/ivo-g/Documents/AutomatedScripts/gitfile/uiautomation/zikaow/'
                   'TestData/login.yml', 'oneclicklogin')
    #
    # def loginByPassword(self, account, password):
    #     self.steps('/Users/ivo-g/Documents/AutomatedScripts/gitfile/uiautomation/zikaow/'
    #                'TestData/login.yml', 'loginByPassword', var1=account, var2=password)
    #
    # def logout(self):
    #     self.steps('/Users/ivo-g/Documents/AutomatedScripts/gitfile/uiautomation/zikaow/'
    #                'TestData/login.yml', 'logout')



