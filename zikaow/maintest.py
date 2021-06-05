import pytest
import os
import shutil


if __name__ == '__main__':
    if os.path.exists('./TestData/report/images/'):
        shutil.rmtree('./TestData/report/images/')
        os.makedirs('./TestData/report/images/')
    else:
        os.makedirs('./TestData/report/images/')

    pytest.main(['-v', 'D:\\gitfile\\uiautomation\\zikaow\\TestCase\\test_login.py::TestLogin',
                 'D:\\gitfile\\uiautomation\\zikaow\\TestCase\\test_booksmall.py::TestMall'])
    # pytest.main(['-v', 'D:\\gitfile\\uiautomation\\zikaow\\TestCase\\
    # test_login.py::TestLogin::test_sms_login_normal'])
    # pytest.main(['-v', 'D:\\gitfile\\uiautomation\\zikaow\\TestCase\\test_booksmall.py::TestMall'])
    os.system(r"allure generate ./TestData/report -o ./TestData/html --clean")
    # os.system('allure open ./TestData/html')


