import allure


class Test001:
    @allure.step("测试计划1")
    def test001(self):
        print("test001")
        allure.attach("data")
        assert True
