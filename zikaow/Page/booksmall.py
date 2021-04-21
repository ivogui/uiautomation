from zikaow.Page.basepage import BasePage


class BooksMall(BasePage):

    def booksmall(self):
        self.steps('../TestData/oneclicklogin.yml', 'booksmall')
