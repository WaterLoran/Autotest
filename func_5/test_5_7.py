import pytest
import allure


class TestFunc5Case7:
    def setup_class(self):
        with allure.step('The setup of the class'):
            pass

    def teardown_class(self):
        with allure.step('The teardown of the class'):
            pass

    @allure.suite('接口测试DEMO')
    @allure.epic('')
    @allure.feature('功能5')
    @allure.title("功能5_具体用例7")
    @allure.description('')
    @pytest.mark.medium
    def test_func5_case7(self):
        with allure.step('step1'):
            assert 1 == 1

