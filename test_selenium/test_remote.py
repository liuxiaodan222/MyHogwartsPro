from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestRemote():
    pass

    def test_remote_chrome(self):
        pass
        driver = webdriver.Chrome()
        # 登录企业微信

        # 通讯录
        driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        # 添加成员

        # 输入姓名
        # 输入账号
        #点击保存

        driver.implicitly_wait(5)
        WebDriverWait
