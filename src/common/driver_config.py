
from appium import webdriver

class Driver_Config():
    def get_driver(self):
        try:
            self.desired_caps = {}
            # 设备信息
            self.desired_caps['platformName'] = 'Android'
            self.desired_caps['platformVersion'] = '5.1.1'
            self.desired_caps['deviceName'] = '127.0.0.1:62001'
            # app的信息
            self.desired_caps['appPackage'] = 'com.android.settings'
            self.desired_caps['appActivity'] = '.Settings'
            self.desired_caps['unicodeKeyboard'] = True
            self.desired_caps['resetKeyboard'] = True

            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)

            return self.driver
        except Exception as e:
            raise e