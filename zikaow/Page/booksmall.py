from zikaow.Page.basepage import BasePage
import requests
import pytest


class BooksMall(BasePage):

    def Books_Mall(self):  # 进入书籍商城
        self.steps('../TestData/booksmall.yml', 'Books_Mall')

    def slide(self, pos, text):  # 书籍商城滑动找书
        if self.isElementPresent('id', 'com.zikao.eduol:id/et_search') is False:
            self.Books_Mall()
        if self.isElementPresent('xpath', f'{self.get_pos(pos)}{self.get_info(text)}') is False:
            self.steps('../TestData/booksmall.yml', 'slide')
            return self.slide(pos, text)
        else:
            return self.get_book_element(pos, text)

    def books_back(self):  # 返回操作
        self.steps('../TestData/booksmall.yml', 'books_back')

    def get_book_list(self):  # 通过requests.get获取接口.json数据
        a = requests.get('https://tk.360xkw.com/crgk/app/shop/getShopProductList?',
                         params={'courseId': '491', 'keyWord': '', 'sort': '0', 'topOrDown': 'false',
                                 'majorId': '0', 'subCourseId': '0', 'pageCurrent': '1', 'pageSize': '254'})
        return a.json()

    def get_value(self, pos, text):  # 筛选接口数据中具体书本的字典表
        # 获取接口数据中的data数据中的records数据列表
        value1 = self.get_book_list().get('data').get('records')
        # 便利records列表，获得具体书本的字典表
        value2 = [d for d in value1 if d['name'] == self.get_book_element(pos, text)][0]
        return value2

    def get_book_element(self, pos, text):  # 拼接位置和书本信息，获取书本文本信息
        element1 = self._driver.find_element_by_xpath(f'{self.get_pos(pos)}{self.get_info(text)}')\
            .get_attribute("text")
        return element1

    def get_pos(self, pos):  # 书城位置xpath，通过pos传递位置坐标
        pos1 = "//*[@class='android.widget.FrameLayout' and @index='%s']" % pos
        return pos1

    def get_info(self, text):  # 书属性xpath，通过text参数传递获取的属性
        info1 = "//*[@resource-id='com.zikao.eduol:id/item_book_%s']" % text
        return info1

    def get_pos_click(self, pos):
        self._driver.find_element_by_xpath(self.get_pos(pos)).click()







