"""
通讯录
"""
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestContact:

    def setup(self):
        caps = {
            "platformName": "android",
            "deviceName": "emulator-5554",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "noReset": "true"

        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_addcontact(self):
        self.driver.find_element("xpath", "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../android.widget.EditText").send_keys("test_02")
        self.driver.find_element(MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']").click()
        sleep(1)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys("18600000002")
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()

        # 添加成功 toast
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")







