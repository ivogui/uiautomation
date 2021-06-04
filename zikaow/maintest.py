import pytest
import os
import shutil

# pytest.main(['-v', './testCase/testDemo.py::TestDemo::test001::tests002',
#              './testCase/testDemo.py::TestDemo::test002'])

if __name__ == '__main__':
    if os.path.exists('./TestData/report/images/'):
        shutil.rmtree('./TestData/report/images/')
        os.makedirs('./TestData/report/images/')
    else:
        os.makedirs('./TestData/report/images/')
    # file_path = os.path.dirname(__file__)
    # aaa = '/TestCase/test_biiksmall.py::TestMall'
    # bbb = '/TestCase/test_login.py::TestLogin'

    # pytest.main(['-v', '])
    pytest.main(['-v', 'D:\\gitfile\\uiautomation\\zikaow\\TestCase\\test_login.py::TestLogin',
                 'D:\\gitfile\\uiautomation\\zikaow\\TestCase\\test_booksmall.py::TestMall'])
    # pytest.main(['-v', 'D:\\gitfile\\uiautomation\\zikaow\\TestCase\\test_booksmall.py::TestMall'])
    os.system(r"allure generate ./TestData/report -o ./TestData/html --clean")


