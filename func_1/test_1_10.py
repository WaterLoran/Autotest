import pytest
import allure


class TestFunc1Case10:
    def setup_class(self):
        with allure.step('The setup of the class'):
            pass

    def teardown_class(self):
        with allure.step('The teardown of the class'):
            pass

    @allure.suite('接口测试DEMO')
    @allure.epic('')
    @allure.feature('功能1')
    @allure.title("功能1_具体用例10")
    @allure.description('')
    @pytest.mark.medium
    def test_func1_case10(self):
        with allure.step('step1'):
            assert 1 == 1

