from zikaow.Page.basepage import BasePage
from zikaow.Page.login import Login
from zikaow.Page.booksmall import BooksMall


# 该类为进入不同页面（对<我的，发现，云村，视频>四个页面建模page的调配page
class Main(BasePage):

    def quit(self):
        self._driver.quit()

    def go_my_login(self):  # 进入我的
        self.steps('/Users/ivo-g/Documents/AutomatedScripts/gitfile/uiautomation/zikaow/'
                   'TestData/main.yml', 'go_my_login')
        return Login(self._driver)

    def go_homepage(self): # 进入首页
        self.steps('D:/Users/ivo-g/Documents/AutomatedScripts/gitfile/uiautomation/zikaow/'
                   'TestData/main.yml', 'go_homepage')
        return BooksMall(self._driver)