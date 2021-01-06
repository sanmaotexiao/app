
from time import sleep


class SlideHandle():
    def __init__(self, driver):
        self.driver = driver

    def add_tysor_swipe(self, n):
        # 下滑操作，（下滑操作时sx不变，变得的是sy，ey）
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        sx = x * 0.05
        sy = y * 0.78
        ey = y * 0.73
        for i in range(n):
            self.driver.swipe(sx, sy, sx, ey)
            sleep(1)