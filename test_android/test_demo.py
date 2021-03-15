from time import sleep

from appium import webdriver
caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "emulator-5554"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["noReset"] = "true"
caps['settings[waitForIdleTimeout]'] = 1
# 客户端与appium 服务器建立连接的代码
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

# 隐式等待
driver.implicitly_wait(5)
sleep(5)
driver.quit()