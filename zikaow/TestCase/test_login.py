
import pytest
from zikaow.Page.app import App


class TestLogin:
    def setup_class(self):  # 类执行运行前执行一次
        self.testDriver = App().restart().main()

    def setup(self):  # 方法运行前执行一次
        self.loginPage = self.testDriver.go_my_login()

    @pytest.mark.parametrize("user, pw, msg", [
        ("", "", "请输入账号"),
        ("1910012989", "", "请输入密码"),
        ("19100129893", "123456", "登入失败,账号或密码错误！"),
        ("19100129893", "000000", "登入失败,账号或密码错误！")
    ])
    @pytest.mark.run(order=1)
    def test_log_error(self, user, pw, msg):   # 测试用例：账号密码错误登录
        self.loginPage.loginByPassword(user, pw)
        self.loginPage.get_toast(msg)
        assert self.loginPage.get_toast(msg) == msg

    @pytest.mark.parametrize("user, pw", [
        ("19100129893", "666666",)
    ])
    @pytest.mark.run(order=2)
    def test_login_normal(self, user, pw):  # 测试用例：账号密码正确登录
        self.loginPage.loginByPassword(user, pw)

    @pytest.mark.run(order=3)
    def test_daily_login(self):   # 测试用例：一键登录
        self.testDriver.go_my_login().oneclicklogin()

    @pytest.mark.parametrize("user, pw, msg", [
        ("", "", "请输入手机号"),
        ("19100129893", "", "请输入验证码"),
        ("19100129", "123456", "账号错误"),
        ("19100129893", "000000", "登录失败，验证码错误")
    ])
    @pytest.mark.run(order=4)
    def test_sms_login_error(self, user, pw, msg):  # 测试用例：验证错错误登录
        self.loginPage.login_SMS(user, pw)
        self.loginPage.get_toast(msg)
        assert self.loginPage.get_toast(msg) == msg

    @pytest.mark.parametrize("user, pw", [
        ("19100129893", "666666",)
    ])
    @pytest.mark.run(order=5)
    def test_sms_login_normal(self, user, pw):  # 测试用例：正确登录；还没有真正的获取验证码，待优化
        self.loginPage.login_SMS(user, pw)

    def teardown(self):  # 方法执行完执行一次
        self.loginPage.back()

    def teardown_class(self):  # 类执行完执行一次
        self.testDriver.quit()
