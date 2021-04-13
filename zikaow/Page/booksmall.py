from zikaow.Page.basepage import BasePage


class BooksMall(BasePage):

    def booksmall(self):
        self.steps('D:/gitfile/uiautomation/zikaow/'
                   'TestData/oneclicklogin.yml', 'booksmall')
