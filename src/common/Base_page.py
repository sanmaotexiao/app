from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time,os

cur_path = os.path.dirname(os.path.realpath(__file__))
screenshot_path = os.path.join(os.path.dirname(cur_path),'screenshots')
if not os.path.exists(screenshot_path):os.mkdir(screenshot_path)


class Base_page():
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        '''重写find_element方法，显式等待'''
        try:
            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            logging.error('页面未找到%s元素'%loc)

    def find_elements(self, *loc):
        '''重写find_element方法，显式等待'''
        try:
            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except Exception as e:
            raise e

    def find_element_by_accessibility_id(self, *loc):
        try:
            time.sleep(3)
            return self.driver.find_element_by_accessibility_id(*loc)
        except Exception as e:
            raise e

    def send_keys(self, value, *loc):
        try:
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError as e:
            raise e

    def getScreenShot(self):
        """重写截图方法"""
        self.sh_file = os.path.join(screenshot_path, '%s.png' % time.strftime('%Y_%m_%d %H:%M:%S'))
        self.driver.get_screenshot_as_file(self.sh_file)