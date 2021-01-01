from appium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.android.contacts'
desired_caps['appActivity'] = '.activities.PeopleActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# desired_caps['appPackage'] = 'com.ss.android.article.news'
# desired_caps['appActivity'] = '.activity.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

driver.find_element_by_id('com.android.contacts:id/floating_action_button').click()
driver.find_element_by_id('com.android.contacts:id/left_button').click()
data = driver.find_element_by_xpath("//*[contains(@text,'姓名')]")
data.send_keys('add')
driver.find_element_by_class_name('android.widget.ImageButton').click()