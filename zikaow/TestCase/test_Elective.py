import shutil
from zikaow.Page.app import App
import pytest
import allure
import os
import threading


@allure.feature('选课模块')
class TestElective:
    def setup_class(self):
        self.testDriver = App().restart().main()
        # shutil.rmtree('../TestCase/report/images/')
        # os.mkdir('../TestCase/report/images/')

    def setup(self):  # 方法运行前执行一次
        self.testElective = self.testDriver.go_Elective()

    def test_a(self):
        pass

    def teardown(self):  # 方法执行完执行一次
        pass

    def teardown_class(self):  # 类执行完执行一次
        self.testDriver.quit()




