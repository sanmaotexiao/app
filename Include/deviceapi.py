from appium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)


#
# print(driver.device_time)
#
# print(driver.get_window_size())

for i in range(3):
    driver.keyevent(25)

driver.quit()


