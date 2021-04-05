from appium import webdriver
from zikaow.Page.basepage import BasePage
from zikaow.Page.main import Main


class App(BasePage):
    # 启动app
    def start(self):
        _package = "com.zikao.eduol"
        _activity = ".activity.LaunchActivity"
        if self._driver is None:
            desir_cap = {
                "appPackage": _package,
                "appActivity": _activity,
                "platformName": "Android",
                "platformVersion": "10",
                # "dontStopAppOnReset": "true",  # 启动程序不要停止被测程序
                "autoGranPermissions": "true",   # 安装时默认配置权限true
                "deviceName": "6de9e7a2"
            }
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desir_cap)
            self._driver.implicitly_wait(8)  # 隐式等待8s
        else:
            self._driver.start_activity(_package, _activity)
        return self

    def restart(self):
        _package = "com.zikao.eduol"
        _activity = ".activity.LaunchActivity"
        if self._driver is None:
            desir_cap = {
                "appPackage": _package,
                "appActivity": _activity,
                "platformName": "Android",
                "platformVersion": "10",
                # "dontStopAppOnReset": "true",     # 启动程序不要停止被测程序
                "noReset": "true",     # 不要清除应用程序数据
                "deviceName": "6de9e7a2"
            }
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desir_cap)
            self._driver.implicitly_wait(8)  # 隐式等待8s
        else:
            self._driver.start_activity(_package, _activity)
        return self

    def main(self):
        return Main(self._driver)