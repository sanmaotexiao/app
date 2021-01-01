import unittest
from src.pages import setting
from src.common import driver_config


class TestLong(unittest.TestCase):
    '''设置页面测试用例'''
    def setUp(self):
        driver = driver_config.Driver_Config()
        self.driver = driver.get_driver()
        # SlideHandle.add_tysor_swipe(self,3)

    def test1 (self):
        '''点击“WLAN”'''
        settings = setting.Setting_page(self.driver)
        settings.click_wlan()
        print(settings.check_wlan_click())
        self.assertEqual(settings.check_wlan_click(),'开启')
        settings.getScreenShot()

    def test2 (self):
        '''点击“蓝牙”'''
        settings = setting.Setting_page(self.driver)
        settings.click_lanya()
        print(settings.check_lanya_click())
        self.assertEqual(settings.check_lanya_click(),'关闭')

    def test3 (self):
        '''点击“更多”'''
        settings = setting.Setting_page(self.driver)
        settings.click_more()
        print(settings.check_more_click())
        self.assertEqual(settings.check_more_click(),'飞行模式')

    def test4 (self):
        '''点击“显示”'''
        settings = setting.Setting_page(self.driver)
        settings.click_show()
        print(settings.check_show_click())
        self.assertEqual(settings.check_show_click(),'亮度')

    def test5(self):
        '''点击“提示音和通知”'''
        settings = setting.Setting_page(self.driver)
        settings.msg_show()
        print(settings.check_msg_click())
        self.assertEqual(settings.check_msg_click(), '声音')

    def test6(self):
        '''点击“存储”'''
        settings = setting.Setting_page(self.driver)
        settings.save_show()
        print(settings.check_msg_click())
        self.assertEqual(settings.check_save_click(), '内部存储空间')

    def test7(self):
        '''点击“电池”'''
        settings = setting.Setting_page(self.driver)
        settings.battery_show()
        print(settings.check_battery_click())
        self.assertEqual(settings.check_battery_click(), '刷新')

    def test8(self):
        '''点击“应用”'''
        settings = setting.Setting_page(self.driver)
        settings.application_show()
        print(settings.check_application_click())
        self.assertEqual(settings.check_application_click(), '已下载')

    def test9(self):
        '''点击“位置信息”'''
        settings = setting.Setting_page(self.driver)
        settings.location_show()
        print(settings.check_location_click())
        self.assertEqual(settings.check_location_click(), '开启')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()