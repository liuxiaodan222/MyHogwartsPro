# 手势解锁
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTouchAction2:

    def setup(self):
        caps = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "cn.kmob.screenfingermovelock",
            "appActivity": "com.samsung.ui.FlashActivity",
            "noReset": "true"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

        self.driver.implicitly_wait(5)

    def teardown(self):

        self.driver.quit()

    def test_touch_action(self):
        # 手势解锁测试

        self.driver.find_element_by_id("cn.kmob.screenfingermovelock:id/topLayout").click()
        sleep(3)
        action = TouchAction(self.driver)
        action.press(x=243, y=395).wait(200).move_to(x=721, y=395).wait(200).move_to(x=1190, y=395).wait(200).move_to(x=1190, y=859)\
            .wait(200).move_to(x=1190, y=1339).release().perform()

        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable)