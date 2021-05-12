from zikaow.Page.app import App
import pytest


class TestLogin:
    def setup_class(self):
        self.testDriver = App().restart().main()

    def setup(self):
        self.BooksMall = self.testDriver.go_homepage()

    def test_go_booksMall(self):
        self.BooksMall.Books_Mall()

    @pytest.mark.parametrize("pos", [pos for pos in range(1, 250)])
    def test_get_book_list(self, pos):
        self.BooksMall.Books_Mall()

        print("--------------b手机数据---------------")
        aa = self.BooksMall.slide(pos, 'title')
        # aa = self.BooksMall.get_book_element(pos, "title")
        print(aa)
        bb = self.BooksMall.slide(pos, 'hint')
        # bb = self.BooksMall.get_book_element(pos, "hint")
        print(bb)
        cc = self.BooksMall.slide(pos, 'price')
        # cc = self.BooksMall.get_book_element(pos, "price")
        cc1 = int(cc)
        print(cc1)
        dd = self.BooksMall.slide(pos, 'sales')
        # dd = self.BooksMall.get_book_element(pos, "sales")
        print(dd)
        print("-------------b接口数据----------------")
        dict1 = self.BooksMall.get_value(pos, 'title')
        print(dict1)
        a = dict1['name']
        print(a)
        b = dict1['briefIntroduction']
        print(b)
        c = dict1['discountPrice']
        print(c)
        d = dict1['sales']
        d1 = f'{d}{"人付款"}'
        print(d1)
        # assert aa == a
        # assert bb == b
        # assert cc1 == c
        # assert dd == d1

    def teardown(self):
        self.BooksMall.books_back()

    def teardown_class(self):
        self.testDriver.quit()
