import pytest
import os
import shutil

# pytest.main(['-v', './testCase/testDemo.py::TestDemo::test001::tests002',
#              './testCase/testDemo.py::TestDemo::test002'])

if __name__ == '__main__':
    if os.path.exists('./TestCase/report/images/'):
        shutil.rmtree('./TestCase/report/images/')
        os.makedirs('./TestCase/report/images/')
    else:
        os.makedirs('./TestCase/report/images/')

    pytest.main(['-v', '\\D:\\gitfile\\uiautomation\\zikaow\\TestCase\\test_login.py::TestLogin'])
    # pytest.main(['-v', '\\D:\\gitfile\\uiautomation\\zikaow\\test_login.py::TestLogin'])
    # os.system(r"allure generate ./TestCase/report -o ./html --clean")


