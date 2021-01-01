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
# desired_caps['appPackage'] = 'com.ss.android.article.news'
# desired_caps['appActivity'] = '.activity.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
# driver.find_element_by_xpath("//*[contains(@text,'蓝牙')]").click()
# driver.swipe(191,1700,191,363,duration=5000)
# start = driver.find_element_by_xpath("//*[contains(@text,'蓝牙')]")
# end = driver.find_element_by_xpath("//*[contains(@text,'安全')]")
# # driver.scroll(end,start)
#
# driver.drag_and_drop(end,start)

driver.background_app(5)

time.sleep(3)
driver.quit()