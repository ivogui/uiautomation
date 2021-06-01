from zikaow.Page.app import App
import pytest
import allure
import os


class TestLogin:
    def setup_class(self):
        self.testDriver = App().restart().main()

    def setup(self):
        self.BooksMall = self.testDriver.go_homepage()

    def test_go_booksMall(self):
        self.BooksMall.Books_Mall()

    @allure.title('书籍商城-商品列表')
    @pytest.mark.parametrize("pos", [pos for pos in range(2, 3)])
    def test_get_book_list(self, pos):
        self.BooksMall.Books_Mall()
        print("--------------b手机数据---------------")
        aaa = ['title', 'hint', 'price', 'sales']
        aa = self.BooksMall.slide(pos, aaa)
        print(aa)
        # bb = self.BooksMall.slide(pos, 'hint')
        # print(bb)
        # cc = self.BooksMall.slide(pos, 'price')
        # cc1 = int(cc)
        # print(cc1)
        # dd = self.BooksMall.slide(pos, 'sales')
        # print(dd)
        # print("-------------b接口数据----------------")
        # dict1 = self.BooksMall.get_value(pos, 'title')
        # print(dict1)
        # a = dict1['name']
        # print(a)
        # b = dict1['briefIntroduction']
        # print(b)
        # c = dict1['discountPrice']
        # print(c)
        # d = dict1['sales']
        # d1 = f'{d}{"人付款"}'
        # print(d1)
        # assert aa == a
        # assert bb == b
        # assert cc1 == c
        # assert dd == d1

    def teardown(self):
        self.BooksMall.books_back()

    def teardown_class(self):
        self.testDriver.quit()
