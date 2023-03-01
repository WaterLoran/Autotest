import pytest
import allure


class TestFunc3Case8:
    def setup_class(self):
        with allure.step('The setup of the class'):
            pass

    def teardown_class(self):
        with allure.step('The teardown of the class'):
            pass

    @allure.suite('接口测试DEMO')
    @allure.epic('')
    @allure.feature('功能3')
    @allure.title("功能3_具体用例8")
    @allure.description('')
    @pytest.mark.medium
    def test_func3_case8(self):
        with allure.step('step1'):
            assert 1 == 1

