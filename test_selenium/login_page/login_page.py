from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.login_page.register_page import RegisterPage


class LoginPage:
    """
    登录页
    """
    def __init__(self, driver):
        self.driver = driver

    def scan_login(self):
        pass

    def goto_register(self):
        """进入注册页"""
        self.driver.find_element(By.XPATH, "//*[@class='login_registerBar_link']").click()
        return RegisterPage(self.driver)