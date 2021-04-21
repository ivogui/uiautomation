from zikaow.Page.basepage import BasePage


class BooksMall(BasePage):

    def Books_Mall(self):  # 进入书籍商城
        self.steps('../TestData/oneclicklogin.yml', 'booksmall')

