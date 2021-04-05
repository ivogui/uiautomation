from zikaow.Page.app import App
import pytest


class TestLogin:
    def setup_class(self):
        self.testDriver = App().restart().main()

    # def setup_method(self):
    #     self.loginPage = self.testDriver.go_my_login()

    # @pytest.mark.parametrize("user, pw", [
    #     ("13823511809", "666666"),
    #     ("1382351180", "666666"),
    #     ("19100129893", "000000")
    # ])

    # def test_log_password(self, user, pw):
    #     self.loginPage.loginByPassword(user, pw)

    def test_daily_login(self):
        self.testDriver.go_my_login().oneclicklogin()

    #
    # def teardown_merhod(self):

    def teardown_class(self):
        self.testDriver.quit()
