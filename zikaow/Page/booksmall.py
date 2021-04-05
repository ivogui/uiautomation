from zikaow.Page.basepage import BasePage


class BooksMall(BasePage):

    def booksmall(self):
        self.steps('/Users/ivo-g/Documents/AutomatedScripts/gitfile/uiautomation/zikaow/'
                   'TestData/oneclicklogin.yml', 'booksmall')