from appium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
# desired_caps['appPackage'] = 'com.tencent.mm'
# desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
desired_caps['noReset'] = True
# desired_caps['appPackage'] = 'com.ss.android.article.news'
# desired_caps['appActivity'] = '.activity.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
# time.sleep(3)
# driver.find_elements_by_id('com.tencent.mm:id/cnh')[2].click()
# time.sleep(3)
# x = driver.get_window_size()["width"]
# y = driver.get_window_size()["height"]
# sx = x * 0.05
# sy = y * 0.78
# ey = y * 0.73
# driver.swipe(sx, sy, sx, ey)
# time.sleep(1)
#
# print(driver.find_elements_by_id('android:id/title'))
# els = driver.find_elements_by_id('android:id/title')
# for i in  els:
#     print(i.text)
# driver.find_elements_by_id('android:id/title')[15].click()

try:
    # driver.find_element_by_id('com.android.settings:id/search').click()
    # driver.find_element_by_id('android:id/search_src_text').send_keys('wla')
    # driver.find_element_by_class_name('android.widget.ImageButton').click()
    # data = driver.find_element_by_id('com.android.settings:id/search').get_attribute('name')
    # print(data)
    # # titles = driver.find_elements_by_id('com.android.settings:id/title')
    # # print(titles)
    # title = driver.find_element_by_name('蓝牙')
    # print(title)
    # title.click()
    driver.find_elements_by_id('com.android.settings:id/title')[7].click()
    # print(driver.find_element_by_xpath("//android.widget.TextView[contains(@content-desc,'刷新')]"))
    # time.sleep(3)
    # t = driver.find_element_by_accessibility_id('刷新')
    # if t is not None:
    #     print(t.get_attribute(name='content-desc') + '======1')  # 搜索或输入网址======1
    #     print(t.get_attribute('name') + '======2')  # text中的内容======2
    #     print(t.text + '======3')  # text中的内容======3
    #     print('OK')
    # else:
    #     print('False')
    time.sleep(3)
    print(driver.find_element_by_xpath("//android.widget.TextView[@text='已下载']").text)
except Exception as e:
    print(e)
finally:
    print('s')

