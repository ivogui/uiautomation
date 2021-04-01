from zikaow.Page.basepage import BasePage


class BooksMall(BasePage):

    def booksmall(self):
        self.steps('D:\\zikaow\\zikaow\\TestData\\login.yml', 'booksmall')