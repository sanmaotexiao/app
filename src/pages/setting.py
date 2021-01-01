
from src.common import Base_page,driver_config
from selenium.webdriver.common.by import By

class Setting_page(Base_page.Base_page):
    #WLAN
    titles = (By.ID,'com.android.settings:id/title')
    print(titles)
    wlan_page = (By.ID,'com.android.settings:id/switch_text')

    lanya_page = (By.ID,'com.android.settings:id/switch_text')

    more_page = (By.ID,'android:id/title')

    show_page = (By.ID,'android:id/title')

    msg_page = (By.ID,'android:id/title')

    save_page = (By.ID, 'android:id/title')

    battery_page = ("刷新")

    application_page = (By.XPATH,"//android.widget.TextView[@text='已下载']")

    location_page = (By.ID,'com.android.settings:id/switch_text')
    #蓝牙

    #更多

    #显示

    #提示音和通知

    #存储

    #电池

    #应用

    #位置信息

    #安全

    #账户

    #语言和输入法

    #备份和重置

    #日期和时间

    #无障碍

    #打印

    #超级用户

    #关于平板电脑

    def click_wlan(self):
        self.driver.find_elements(*self.titles)[0].click()

    def click_lanya(self):
        self.driver.find_elements(*self.titles)[1].click()

    def click_more(self):
        self.driver.find_elements(*self.titles)[2].click()

    def click_show(self):
        self.driver.find_elements(*self.titles)[3].click()

    def msg_show(self):
        self.driver.find_elements(*self.titles)[4].click()

    def save_show(self):
        self.driver.find_elements(*self.titles)[5].click()

    def battery_show(self):
        self.driver.find_elements(*self.titles)[6].click()

    def application_show(self):
        self.driver.find_elements(*self.titles)[7].click()

    def location_show(self):
        self.driver.find_elements(*self.titles)[8].click()

    #check

    def check_wlan_click(self):
        return self.find_element(*self.wlan_page).text

    def check_lanya_click(self):
        return self.find_element(*self.lanya_page).text

    def check_more_click(self):
        return self.find_elements(*self.more_page)[0].text

    def check_show_click(self):
        return self.find_elements(*self.show_page)[0].text

    def check_msg_click(self):
        return self.find_elements(*self.msg_page)[0].text

    def check_save_click(self):
        return self.find_elements(*self.save_page)[0].text

    def check_battery_click(self):
        return self.find_element_by_accessibility_id(self.battery_page).text

    def check_application_click(self):
        return self.find_element(*self.application_page).text

    def check_location_click(self):
        return self.find_element(*self.location_page).text
