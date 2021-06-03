import shutil
from zikaow.Page.app import App
import pytest
import allure
import os
import threading


@allure.feature('书城模块')
class TestMall:
    def setup_class(self):
        self.testDriver = App().restart().main()
        shutil.rmtree('../TestCase/report/images/')
        os.mkdir('../TestCase/report/images/')

    def setup(self):
        self.BooksMall = self.testDriver.go_homepage()

    def test_go_booksMall(self):
        self.BooksMall.Books_Mall()

    # @allure.title('搜索')
    # def test_as(self):
    #     pass
    # @allure.title('筛选')
    # def test_ba(self):
    #     pass
    # @allure.title('商品详情：评论点赞+推荐课程')
    # def test_ba(self):
    #     pass
    # @allure.title('确认订单：支付方式+学生留言+支付')
    # def test_ba(self):
    #     pass
    # @allure.title('分享+交流群')
    # def test_ba(self):
    #     pass

    @allure.title('书籍商城-商品列表')
    @pytest.mark.parametrize("pos", [pos for pos in range(1, 10)])
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
        print(d)
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
                           '书籍详情', attachment_type=allure.attachment_type.PNG)
        print("-------------v付款页面----------------")
        self.BooksMall.steps('../TestData/booksmall.yml', 'buy')
        fa = self.BooksMall.get_element("id", "com.zikao.eduol:id/pay_confirm_detail_title", "text")
        print(fa)
        fb = self.BooksMall.get_element("id", "com.zikao.eduol:id/pay_confirm_detail_hint", "text")
        print(fb)
        fc = self.BooksMall.get_element("id", "com.zikao.eduol:id/pay_confirm_detail_price", "text")
        print(fc)
        allure.attach.file(self.BooksMall.get_screen('../TestCase/report/images/'),
                           '付款页面', attachment_type=allure.attachment_type.PNG)
        self.BooksMall.books_back()

        assert aa == a
        assert aa == aaa
        assert aa == fa

        assert bb[:10] == b[:10]
        assert bb[:10] == bbb[:10]
        assert bb[:10] == fb[:10]

        assert int(cc) == c
        assert cc == ccc
        assert cc == fc

        assert int(dd[:-3]) == d
        assert dd[:-3] == ddd[:-3]

    def teardown(self):
        self.BooksMall.books_back()

    def teardown_class(self):
        self.testDriver.quit()
