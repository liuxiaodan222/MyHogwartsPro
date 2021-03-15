from time import sleep

from test_selenium.login_page.main_page import MainPage


class TestRegister:

    def test_register(self):
        # 链式调用
        main = MainPage()
        main.goto_register().register()
        sleep(5)

    def test_login_register(self):
        # 首页 - 登录页 - 企业注册
        main = MainPage()
        main.goto_login().goto_register().register()