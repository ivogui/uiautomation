import shutil
from zikaow.Page.app import App
import pytest
import allure
import os
import threading


class TestLogin:
    def setup_class(self):
        self.testDriver = App().restart().main()
        shutil.rmtree('../TestCase/report/images/')
        os.mkdir('../TestCase/report/images/')

    def setup(self):
        self.BooksMall = self.testDriver.go_homepage()

    def test_go_booksMall(self):
        self.BooksMall.Books_Mall()

    @allure.title('书籍商城-商品列表')
    @pytest.mark.parametrize("pos", [pos for pos in range(4, 10)])
    def test_get_book_list(self, pos):
        print("--------------b手机数据---------------")
        aa = self.BooksMall.slide(pos, 'title')
        print(aa)
        bb = self.BooksMall.slide(pos, 'hint')
        print(bb)
        cc = self.BooksMall.slide(pos, 'price')
        print(cc)
        dd = self.BooksMall.slide(pos, 'sales')
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
        print("-------------m书籍详情----------------")
        self.BooksMall.get_pos_click(pos)
        aaa = self.BooksMall.get_element("id", "com.zikao.eduol:id/shop_detail_name", "text")
        print(aaa)
        bbb = self.BooksMall.get_element("id", "com.zikao.eduol:id/shop_detail_hint", "text")
        print(bbb)
        ccc = self.BooksMall.get_element("id", "com.zikao.eduol:id/shop_detail_price", "text")
        print(ccc)
        ddd = self.BooksMall.get_element("id", "com.zikao.eduol:id/shop_detail_count", "text")
        print(ddd)
        allure.attach.file(self.BooksMall.get_screen('../TestCase/report/images/'),
                           attachment_type=allure.attachment_type.PNG)
        print("-------------v付款页面----------------")
        self.BooksMall.steps('../TestData/booksmall.yml', 'buy')
        fa = self.BooksMall.get_element("id", "com.zikao.eduol:id/pay_confirm_detail_title", "text")
        print(fa)
        fb = self.BooksMall.get_element("id", "com.zikao.eduol:id/pay_confirm_detail_hint", "text")
        print(fb)
        fc = self.BooksMall.get_element("id", "com.zikao.eduol:id/pay_confirm_detail_price", "text")
        print(fc)
        self.BooksMall.books_back()
        assert aa == a
        assert aa == aaa
        assert aa == fa

        # assert bb == b
        # assert bb == bbb
        # assert bb == fb

        assert int(cc) == c
        assert cc == ccc
        assert cc == fc
        # assert  == fb

        assert dd == d1

    def teardown(self):
        self.BooksMall.books_back()

    def teardown_class(self):
        self.testDriver.quit()
