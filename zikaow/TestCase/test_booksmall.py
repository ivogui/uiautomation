from zikaow.Page.app import App
import pytest


class TestLogin:
    def setup_class(self):
        self.testDriver = App().restart().main()

    def setup(self):
        self.BooksMall = self.testDriver.go_homepage()

    def test_go_booksMall(self):
        self.BooksMall.Books_Mall()

    @pytest.mark.parametrize("pos", [pos for pos in range(1, 10)])
    def test_get_book_list(self, pos):
        while True:
            if self.testDriver.isElementPresent("id", "com.zikao.eduol:id/bottom_line_tv") is True:
                break
            elif self.testDriver.isElementPresent('xpath', self.BooksMall.get_pos(pos)) is False:
                self.testDriver.steps('../TestData/booksmall.yml', 'slide')
            else:
                print("--------------a---------------")
                aa = self.BooksMall.get_book_element(pos, "title")
                print(aa)
                bb = self.BooksMall.get_book_element(pos, "hint")
                print(bb)
                cc = self.BooksMall.get_book_element(pos, "price")
                print(cc)
                dd = self.BooksMall.get_book_element(pos, "sales")
                print(dd)
                print("--------------b---------------")
                dict1 = self.BooksMall.get_value(pos, 'title')
                print(dict1)
                a = dict1['name']
                print(a)
                b = dict1['discountPrice']
                print(b)
                c = dict1['sales']
                print(c)
                d = dict1['briefIntroduction']
                print(d)

    # def teardown(self):
    #     self.BooksMall.books_back()

    def teardown_class(self):
        self.testDriver.quit()
