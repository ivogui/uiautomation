from zikaow.Page.basepage import BasePage
import requests


class BooksMall(BasePage):
    bookList = []
    Bookinformation = []
    ConfirmOrder = {}

    def Books_Mall(self):  # 进入书籍商城
        self.steps('../TestData/booksmall.yml', 'Books_Mall')

    def slide(self):
        self.steps('../TestData/booksmall.yml', 'Books_Mall')
        while True:
            if self.isElementPresent("xpath", "//*[@class='android.widget.FrameLayout' "
                                              "and @index='1']") is False:
                self.steps('../TestData/booksmall.yml', 'bookList')
            elif self.isElementPresent("xpath", "//*[@class='android.widget.FrameLayout' "
                                                "and @index='1']") is True:
                pass

            elif self.isElementPresent("id", "com.zikao.eduol:id/bottom_line_tv") is True:
                break

        # self.bookDetails = self.steps('../TestData/booksmall.yml', 'bookDetails')
        # self.ConfirmOrder = self.steps('../TestData/booksmall.yml', 'ConfirmOrder')

    def books_back(self):  # 返回操作
        self.steps('../TestData/booksmall.yml', 'books_back')

    def get_book_list(self):
        a = requests.get('https://tk.360xkw.com/crgk/app/shop/getShopProductList?',
                         params={'courseId': '491', 'keyWord': '', 'sort': '0', 'topOrDown': 'false',
                                 'majorId': '0', 'subCourseId': '0', 'pageCurrent': '1', 'pageSize': '254'})
        return a

    def get_book_element(self, pos, info):
        s1 = "//*[@class='android.widget.FrameLayout' and @index='%s']" % pos
        s2 = "%s" % info
        element = self.find("xpath", f'{s1}{s2}')
        return element

    def get_pos(self):
        pass

    def get_info(self, path):
        pass

