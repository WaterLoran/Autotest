import pytest
import allure


class TestFunc4Case1:
    def setup_class(self):
        with allure.step('The setup of the class'):
            pass

    def teardown_class(self):
        with allure.step('The teardown of the class'):
            pass

    @allure.suite('接口测试DEMO')
    @allure.epic('')
    @allure.feature('功能4')
    @allure.title("功能4_具体用例1")
    @allure.description('')
    @pytest.mark.medium
    def test_func4_case1(self):
        with allure.step('step1'):
            assert 1 == 1

