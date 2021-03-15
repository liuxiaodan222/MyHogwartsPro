# TouchAction
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "emulator-5554"
caps["appPackage"] = "com.tencent.wework"
caps["appActivity"] = ".launch.LaunchSplashActivity"
caps["noReset"] = "true"
caps['settings[waitForIdleTimeout]'] = 1
# 客户端与appium 服务器建立连接的代码
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

action = TouchAction(driver)


window_rect = driver.get_window_rect() # 获取屏幕尺寸
width = window_rect["width"]
height = window_rect["height"]
x1 = int(width/2)
y_start = int(height * 0.8)
y_end = int(height * 0.2)
# 从下往上滑动页面
action.press(x=x1, y=y_start).wait(200).move_to(x=x1 ,y=y_end).release().perform()


