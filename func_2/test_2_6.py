import pytest
import allure


class TestFunc2Case6:
    def setup_class(self):
        with allure.step('The setup of the class'):
            pass

    def teardown_class(self):
        with allure.step('The teardown of the class'):
            pass

    @allure.suite('接口测试DEMO')
    @allure.epic('')
    @allure.feature('功能2')
    @allure.title("功能2_具体用例6")
    @allure.description('')
    @pytest.mark.medium
    def test_func2_case6(self):
        with allure.step('step1'):
            assert 1 == 1

