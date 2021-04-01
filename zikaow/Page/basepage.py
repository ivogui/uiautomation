
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.touch_action import TouchAction
import yaml
import pytest
from time import sleep

from typing import List

'''创建一个基础页面类，用于封装公共模块的处理方法
   和根据yaml配置文件进行案例的测试步骤'''


class BasePage:
    _blackList = []  # 黑名单列表，用于处理再case运行过程中可能出现的未知弹窗
    _errorCount = 0  # 定位元素的错误次数，元素定位中可能出现一次定位不到
    _errorMax = 5  # 允许进行元素定位的最大错误次数

    def __init__(self, driver: WebDriver = None):  # 初始化driver
        self._driver = driver

    def find(self, by, locator):  # $by>定位元素的方法，$locator>定位元素对应的所需value
        try:
            if isinstance(by, tuple):  # 如果传入的定位是个元组形式，包括方法和locator，就进行解包的方式定位
                element = self._driver.find_element(*by)
            else:
                element = self._driver.find_element(by, locator)
            self._errorCount = 0  # 找到元素，错误次数为0
            return element
        except Exception as e:
            self._errorCount += 1  # 未找到该元素，错误次数加1
            if self._errorCount >= self._errorMax:
                raise e  # 错误次数大于设置的最大次数抛出异常
            for black in self._blackList:
                elements = self._driver.find_elements(*black)  # 找到黑名单列表里的所有元素,[(by, locator),]的形式设置
                if len(elements) > 0:  # 出现弹框匹配黑名单列表大于0，即出现未知弹框
                    elements[0].click()  # 点击过后就找不到该元素了，所以永远点击第一个找到的就可以了
                    return self.find(by, locator)  # 点击后返回原方法，轮询去让定位可以继续执行
            raise e  # 没有找到，抛出异常

    def send(self, by, locator, value):  # 数据输入的方法
        try:
            self._driver.find(by, locator).send_keys(value)  # 定位到输入的位置，输入值
            self._errorCount = 0
        except Exception as e:
            self._errorCount += 1
            if self._errorCount >= self._errorMax:
                raise e  # 大于错误次数，抛出异常
            for black in self._blackList:
                elements = self._driver.find_element(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(by, locator)
            raise e

    def steps(self, path, key):  # 定义操作步骤的方法，用于通过编写配置文件，执行相关用例
        with open(path, 'r', encoding='utf-8') as f:
            steps: List[dict] = yaml.safe_load(f)  # 操作步骤的数据类型为：[{},{}]
            po_method = steps[key]
            # if po_method.keys().__contains__("elements"):
            #     po_elements = steps['elements']
            # 遍历操作步骤
            for step in po_method:
                if 'by' in step.keys():
                    element = self.find(step['by'], step['locator'])  # 定位到元素
            # for step in po_method:
            #     if step.keys().__contains__("element"):
            #         element_platform = po_elements[step['element']]
            #     else:
            #         element_platform = {"by": step['by'], "locator": step['locator']}
            #     element: WebElement = self.find(by=element_platform['by'], locator=element_platform['locator'])

                # 要进行的动作操作
                if 'action' in step.keys():
                    if 'click' == step['action']:  # 点击操作
                        element.click()
                    if 'send' == step['action']:
                        element.send_keys(step['value'])
                    if 'TouchAction' in step['action']:  # 滑动操作
                        action = TouchAction(self._driver)
                        action.press(x=step['value'][0]['x_start'], y=step['value'][0]['y_start']).wait(300) \
                            .move_to(x=step['value'][1]['x_end'], y=step['value'][1]['y_end']).release().perform()
                # 断言
                if 'assertion' in step.keys():
                    if "sleep" in step['assertion'].keys():
                        sleep(step['assertion']['sleep'])
                        element = self.find(step['assertion']['by'], step['assertion']['locator'])
                        attribute = element.get_attribute(step['assertion']['attribute'])
                        pytest.assume(attribute == step['assertion']['assert_info'])
                    if 'back' in step.keys():
                        self._driver.back()
