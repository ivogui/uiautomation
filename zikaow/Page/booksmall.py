from zikaow.Page.basepage import BasePage


class BooksMall(BasePage):
    bookList = []
    bookDetails = {}
    ConfirmOrder = {}

    def Books_Mall(self):  # 进入书籍商城
        self.steps('../TestData/booksmall.yml', 'Books_Mall')

    def TextComparison(self):
        self.steps('../TestData/booksmall.yml', 'Books_Mall')
        while True:
            self.steps('../TestData/booksmall.yml', 'bookList')
            if self.isElementPresent("id", "com.zikao.eduol:id/bottom_line_tv") is True:
                break

        # self.bookDetails = self.steps('../TestData/booksmall.yml', 'bookDetails')
        # self.ConfirmOrder = self.steps('../TestData/booksmall.yml', 'ConfirmOrder')

    def books_back(self):  # 返回操作
        self.steps('../TestData/booksmall.yml', 'books_back')
