from zikaow.Page.app import App

import pytest


class TestLogin:
    def setup_class(self):
        self.testDriver = App().start().main()

    def setup_method(self):
        self.loginPage = self.testDriver.go_my_login()

    def teardown_class(self):
        self.testDriver.quit()

    def test_daily_login(self):
        self.testDriver.go_my_login().login()
