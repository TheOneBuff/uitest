# -*- coding:utf-8 _*-
# coding=utf-8
"""
@Time: 2023/8/13 14:46
@Auth: 王浩鹏
@File ：login_page.py
"""
from selenium.webdriver.common.by import By
from utils.driver import get_driver


class LoginPage:
    url = '/login.html'
    username_input = (By.ID, 'username')
    password_input = (By.ID, 'password')
    login_button = (By.ID, 'login-button')

    def __init__(self):
        self.driver = get_driver()

    def open(self):
        self.driver.get(get_base_url() + self.url)

    def close(self):
        self.driver.quit()

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()