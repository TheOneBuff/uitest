import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from utils import request_util
from utils.take_screenshot import take_screenshot
from utils import read_config
from utils.driver import get_driver


class edit_point:
    url = read_config.get_edit_url()

    def __init__(self):
        self.driver = get_driver()
        self.driver.maximize_window()

    def get_minder_node_id(self, driver):
        for i in range(1000):
            try:
                driver.find_elements(By.ID, 'minder_node%s' % str(i + 1))[0]
            except:
                return i

    def add_sub_theme(self):
        self.driver.get(self.url)
        time.sleep(10)
        root_node = self.driver.find_element(By.ID, 'node_outline1')
        ActionChains(self.driver).context_click(root_node).perform()
        take_screenshot(self.driver, '添加子主题')
        click_sub_theme = [em for em in self.driver.find_elements(By.CLASS_NAME, 'menu-item-name') if em.text == '新增子主题']
        ActionChains(self.driver).click(click_sub_theme[0]).perform()
        time.sleep(3)
        if request_util.update_node_name():
            self.driver.refresh()
            time.sleep(10)
            id = self.get_minder_node_id(self.driver)
            childnode = self.driver.find_element(By.ID, 'minder_node%s' % str(id))
            ActionChains(self.driver).context_click(childnode).perform()
            defined = [em for em in self.driver.find_elements(By.CLASS_NAME, 'menu-item-name') if em.text == '需求定义']
            ActionChains(self.driver).click(defined[0]).perform()
            time.sleep(5)
            self.driver.find_element(By.ID, 'definition').send_keys('UI测试指标定义')
            take_screenshot(self.driver, '需求定义')
            time.sleep(5)
            zhibiaodingyi = [em for em in self.driver.find_elements(By.CLASS_NAME, 'ant-tabs-tab-btn') if em.text == '指标定义']
            ActionChains(self.driver).click(zhibiaodingyi[0]).perform()
            time.sleep(2)
            tianjiazhibiao = [em for em in self.driver.find_elements(By.TAG_NAME, 'span') if em.text == '添加指标']
            ActionChains(self.driver).click(tianjiazhibiao[0]).perform()
            time.sleep(2)
            self.driver.find_element(By.ID, 'indicatorName').send_keys('UI测试')
            self.driver.find_element(By.ID, 'indexAbbreviation').send_keys('UI测试名')
            self.driver.find_element(By.ID, 'sourceWind_edbIndicatorId').send_keys('m0000004')
            take_screenshot(self.driver, '添加指标')
            time.sleep(2)
            zhishidiandingyi = [em for em in self.driver.find_elements(By.CLASS_NAME, 'ant-tabs-tab-btn') if em.text == '知识点定义']
            ActionChains(self.driver).click(zhishidiandingyi[0]).perform()
            xinzengzhishidian = [em for em in self.driver.find_elements(By.TAG_NAME, 'span') if em.text == '添加知识点']
            ActionChains(self.driver).click(xinzengzhishidian[0]).perform()
            time.sleep(2)
            input = self.driver.find_element(By.CLASS_NAME, 'ant-select-selection-overflow')
            ActionChains(self.driver).click(input).perform()
            time.sleep(2)
            ele = [em for em in self.driver.find_elements(By.CLASS_NAME, 'ant-select-item-option-content') if em.text == 'UI测试']
            ActionChains(self.driver).click(ele[0]).perform()
            take_screenshot(self.driver, '添加知识点')
            print("sucessed")
            time.sleep(1)
            ele = [em for em in self.driver.find_elements(By.CLASS_NAME, 'ant-btn.ant-btn-default') if em.text == '保存需求']
            ActionChains(self.driver).click(ele[0]).perform()
            time.sleep(2)
            self.driver.refresh()
            time.sleep(10)
            id = self.get_minder_node_id(self.driver)
            childnode = self.driver.find_element(By.ID, 'minder_node%s' % str(id))
            ActionChains(self.driver).context_click(childnode).perform()
            time.sleep(2)
            defined = [em for em in self.driver.find_elements(By.CLASS_NAME, 'menu-item-name') if em.text == '需求提交']
            ActionChains(self.driver).click(defined[0]).perform()
            time.sleep(1)
            ele = [em for em in self.driver.find_elements(By.CLASS_NAME, 'ant-btn.ant-btn-primary') if em.text == '确 认']
            ActionChains(self.driver).click(ele[0]).perform()
            self.close()

    def close(self):
        self.driver.quit()



