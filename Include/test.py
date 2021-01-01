from appium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
# desired_caps['appPackage'] = 'com.ss.android.article.news'
# desired_caps['appActivity'] = '.activity.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
# print(driver.is_app_installed('com.ss.android.article.news'))
# driver.remove_app('com.ss.android.article.news')
# print(driver.is_app_installed('com.ss.android.article.news'))
# try:
    # driver.find_element_by_class_name('android.widget.LinearLayout').click()
    # time.sleep(2)
    # driver.find_element_by_class_name('android.widget.ImageButton').click()
    # time.sleep(2)
    # el_list = driver.find_elements_by_id('com.android.settings:id/title')

    # for i in el_class_list :
    #     if i.text == '安全':
    #         i.click()
    #         time.sleep(2)
    #         break
#     el_class_list = driver.find_elements_by_class_name('android.widget.TextView')
#     for i in el_class_list:
#         if 'WLAN' in i.text:
#             i.click()
#             time.sleep(2)
#             break
# except Exception as e:
#     print(e)
# finally:
#     driver.quit()

print(time.strftime('%H:%M:%S',time.localtime()))
el = WebDriverWait(driver,timeout=5,poll_frequency=0.5).until(lambda x: x.find_element_by_xpath("//*[contains(@text,'WLA')]"))
el.click()
time.sleep(2)
print(time.strftime('%H:%M:%S',time.localtime()))