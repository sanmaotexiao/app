import unittest
from src.pages import setting
from src.common import driver_config
import sys


class Test_Setting_Page(unittest.TestCase):
    """设置页面测试用例"""
    def setUp(self):
        driver = driver_config.Driver_Config()
        self.driver = driver.get_driver()

    def test1 (self):
        """点击'WLAN'"""
        settings = setting.Setting_page(self.driver)
        settings.click_wlan()
        print(settings.check_wlan_click())
        self.assertEqual(settings.check_wlan_click(),'开启')
        # img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//screenshots//'
        # if not os.path.exists(img_folder): os.mkdir(img_folder)
        # times = time.strftime('%Y-%m-%d_%H_%M_%S_')
        # print(times)
        # sh_file = img_folder + times + '.png'
        # print(sh_file)
        # print(self.driver.get_screenshot_as_file(sh_file))
        # self.driver.get_screenshot_as_file(sh_file)
        settings.getscreenshot(sys._getframe().f_code.co_name)

    def test2 (self):
        '''点击“蓝牙”'''
        settings = setting.Setting_page(self.driver)
        settings.click_lanya()
        print(settings.check_lanya_click())
        self.assertEqual(settings.check_lanya_click(),'关闭')
        settings.getscreenshot(sys._getframe().f_code.co_name)

    # def test3 (self):
    #     '''点击“更多”'''
    #     settings = setting.Setting_page(self.driver)
    #     settings.click_more()
    #     print(settings.check_more_click())
    #     self.assertEqual(settings.check_more_click(),'飞行模式')
    #     settings.getscreenshot(sys._getframe().f_code.co_name)
    #
    # def test4 (self):
    #     '''点击“显示”'''
    #     settings = setting.Setting_page(self.driver)
    #     settings.click_show()
    #     print(settings.check_show_click())
    #     self.assertEqual(settings.check_show_click(),'亮度')
    #     settings.getscreenshot(sys._getframe().f_code.co_name)
    #
    # def test5(self):
    #     '''点击“提示音和通知”'''
    #     settings = setting.Setting_page(self.driver)
    #     settings.msg_show()
    #     print(settings.check_msg_click())
    #     self.assertEqual(settings.check_msg_click(), '声音')
    #     settings.getscreenshot(sys._getframe().f_code.co_name)
    #
    # def test6(self):
    #     '''点击“存储”'''
    #     settings = setting.Setting_page(self.driver)
    #     settings.save_show()
    #     print(settings.check_msg_click())
    #     self.assertEqual(settings.check_save_click(), '内部存储空间')
    #     settings.getscreenshot(sys._getframe().f_code.co_name)
    #
    # def test7(self):
    #     '''点击“电池”'''
    #     settings = setting.Setting_page(self.driver)
    #     settings.battery_show()
    #     print(settings.check_battery_click())
    #     self.assertEqual(settings.check_battery_click(), '刷新')
    #     settings.getscreenshot(sys._getframe().f_code.co_name)
    #
    # def test8(self):
    #     '''点击“应用”'''
    #     settings = setting.Setting_page(self.driver)
    #     settings.application_show()
    #     print(settings.check_application_click())
    #     self.assertEqual(settings.check_application_click(), '已下载')
    #     settings.getscreenshot(sys._getframe().f_code.co_name)
    #
    # def test9(self):
    #     '''点击“位置信息”'''
    #     settings = setting.Setting_page(self.driver)
    #     settings.location_show()
    #     print(settings.check_location_click())
    #     self.assertEqual(settings.check_location_click(), '开启')
    #     settings.getscreenshot(sys._getframe().f_code.co_name)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()