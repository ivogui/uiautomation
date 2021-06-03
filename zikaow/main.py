import pytest
import os

# pytest.main(['-v', './testCase/testDemo.py::TestDemo::test001::tests002',
#              './testCase/testDemo.py::TestDemo::test002'])

if __name__ == '__main__':
    # pytest.main(["-sq", "--emoji"])
    os.system(r"allure generate ./report -o ./html --clean")
    pytest.main(['-v', './TestCase/test_login.py::TestLogin',
                 './TestCase/test_booksmall.py::TestMall'])

