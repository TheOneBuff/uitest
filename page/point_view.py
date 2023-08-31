import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from utils import request_util
from utils.take_screenshot import take_screenshot
from utils import read_config
from utils.driver import get_driver


class point_view:
    url = read_config.get_pointview_url()

    def __init__(self):
        self.driver = get_driver()
        self.driver.maximize_window()

    def close(self):
        self.driver.quit()


    def point_view(self):
        self.driver.get(self.url)
        time.sleep(5)
        take_screenshot(self.driver, '查看结果')
        return self.driver.find_element(By.ID, 'kity_text_22').text
