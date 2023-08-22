import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from utils import read_config
from utils.driver import get_driver
from utils.take_screenshot import take_screenshot


class edit_point:
    url = read_config.get_edit_url()

    def __init__(self):
        self.driver = get_driver()
        self.driver.maximize_window()

    def edit(self):
        self.driver.get(self.url)
        # 获取新增知识点坐标并且点击
        time.sleep(3)
        span_em = self.driver.find_elements(By.TAG_NAME, 'span')
        time.sleep(3)
        for span in span_em:
            if span.text == "新增知识点":
                ActionChains(self.driver).click(span).perform()
                # 获取图表并且点击
                table = self.driver.find_elements(By.ID, 'tabs-tab-2')

                ActionChains(self.driver).click(table).perform()
                break
        take_screenshot(self.driver, 'add')

    def close(self):
        self.driver.quit()

