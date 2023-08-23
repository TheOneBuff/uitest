import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from utils.driver import get_driver
import os
from configparser import ConfigParser

from utils.take_screenshot import take_screenshot

config = ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '..\\config\\config.ini'))

add_point_url = config.get('URL', 'add_point_url')
class add_point:
    url = add_point_url

    def __init__(self):
        self.driver = get_driver()
        self.driver.maximize_window()

    def add(self):
        self.driver.get(add_point_url)
        # 获取新增知识点坐标并且点击
        time.sleep(3)
        span_em = self.driver.find_elements(By.TAG_NAME, 'span')
        time.sleep(3)
        for span in span_em:
            if span.text == "新增知识c点":
                ActionChains(self.driver).click(span).perform()
                # 获取图表并且点击
                table = self.driver.find_elements(By.ID, 'tabs-tab-2')

                ActionChains(self.driver).click(table).perform()
                break
        take_screenshot(self.driver, 'add')

    def close(self):
        self.driver.quit()

