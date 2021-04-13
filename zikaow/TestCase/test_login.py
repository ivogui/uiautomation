from zikaow.Page.app import App
import pytest


class TestLogin:
    def setup_class(self):
        self.testDriver = App().restart().main()

    def setup(self):
        self.loginPage = self.testDriver.go_my_login()

    @pytest.mark.parametrize("user, pw, msg", [
        ("13823511809", "666666", "登陆失败，账号或密码错误"),
        ("1910012989", "666666", "登陆失败，账号或密码错误"),
        ("19100129893", "666666", "登陆失败，账号或密码错误"),
        ("19100129893", "000000", "登陆失败，账号或密码错误")
    ])
    @pytest.mark.run(order=1)
    def test_log_password(self, user, pw, msg):
        self.loginPage.loginByPassword(user, pw)
        assert msg in self.loginPage.getErrorMsg()

    @pytest.mark.run(order=2)
    def test_login_out(self):
        self.loginPage.logout()

    @pytest.mark.run(order=3)
    def test_daily_login(self):
        self.testDriver.go_my_login().oneclicklogin()

    def teardown(self):
        self.loginPage.back()

    def teardown_class(self):
        self.testDriver.quit()
