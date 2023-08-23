import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from utils import read_config
from utils.driver import get_driver
from utils.take_screenshot import take_screenshot
import requests
import json


class edit_point:
    url = read_config.get_edit_url()


    def __init__(self):
        self.driver = get_driver()
        self.driver.maximize_window()
    def update_node_name(self):
        heands = {"Connection": "keep-alive",
                  "Content-Type": "application/json;charset=UTF-8",
                  "Cookies": "JSESSIONID=CD579C23A983C7520F3A708DB714D312; JSESSIONID=4072DE381BBB6DAF8A1BBE6FAFE9FE6B"
                  }
        data = {"nodeId": "6dba5d45-a252-484d-9abe-fec8505c16ee",
                "name": "自动创建_%s" % time.strftime('%Y%m%d_%H_%M_%S',time.localtime()),
                "nameEn": "",
                "lang": "zh",
                "authProjectId": "10",
                "treeId": "ZGHG"}
        response = requests.get(read_config.get_nodeId_url(), headers=heands)
        if response.status_code == 200:
            data['nodeId'] = json.loads(response.text)['data']['children'][-1]['nodeId']
            response = requests.post(read_config.post_update_url(), headers=heands, data=json.dumps(data))
            if response.status_code == 200:
                return True
            else:
                return False

    def get_minder_node_id(self, driver):
        for i in range(1000):
            try:
                driver.find_elements(By.ID, 'minder_node%s' % str(i + 1))[0]
            except:
                return i


    def add_first_node(self):
        self.driver.get(self.url)
        time.sleep(10)
        root_node = self.driver.find_element(By.ID, 'node_outline1')
        ActionChains(self.driver).context_click(root_node).perform()
        take_screenshot(self.driver, 'add_first_node')
        click_sub_theme = [em for em in self.driver.find_elements(By.CLASS_NAME, 'menu-item-name') if em.text == '新增子主题']
        ActionChains(self.driver).click(click_sub_theme[0]).perform()
        time.sleep(3)
        if self.update_node_name():
            self.driver.refresh()
            time.sleep(10)
            id = self.get_minder_node_id(self.driver)
            childnode = self.driver.find_element(By.ID, 'minder_node%s' % str(id))
            ActionChains(self.driver).context_click(childnode).perform()
            defined = [em for em in self.driver.find_elements(By.CLASS_NAME, 'menu-item-name') if em.text == '需求定义']
            ActionChains(self.driver).click(defined[0]).perform()
            time.sleep(5)
            self.driver.find_element(By.ID, 'definition').send_keys('UI测试指标定义')
            time.sleep(5)
            zhibiaodingyi = [em for em in self.driver.find_elements(By.CLASS_NAME, 'ant-tabs-tab-btn') if em.text == '需求定义']
            ActionChains(self.driver).click(zhibiaodingyi[0]).perform()
            time.sleep(10)
            tianjiazhibiao = self.driver.find_element(By.CLASS_NAME, 'anticon.anticon-plus-circle')
            ActionChains(self.driver).click(tianjiazhibiao).perform()
            self.driver.find_element(By.ID, 'indicatorName').send_keys('UI测试')
            self.driver.find_element(By.ID, 'indexAbbreviation').send_keys('UI测试名')
            self.driver.find_element(By.ID, 'definition').send_keys('UI测试指标定义')
            self.driver.find_element(By.ID, 'sourceWind_edbIndicatorId').send_keys('m00c0004')
            time.sleep(10)
            zhishidiandingyi = [em for em in self.driver.find_elements(By.CLASS_NAME, 'ant-tabs-tab-btn') if em.text == '知识点定义']
            ActionChains(self.driver).click(zhishidiandingyi[0]).perform()
            xinzengzhishidian = self.driver.find_element(By.CLASS_NAME, 'anticon.anticon-plus-circle')
            ActionChains(self.driver).click(xinzengzhishidian).perform()



    def close(self):
        self.driver.quit()

