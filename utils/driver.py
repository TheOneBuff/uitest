# -*- coding:utf-8 _*-
# coding=utf-8
"""
@Time: 2023/8/13 14:44
@Auth: 王浩鹏
@File ：driver.py.py
"""
import os
from selenium import webdriver
from configparser import ConfigParser


def get_driver():
    config = ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '../config/config.ini'))

    browser_name = config.get('Browser', 'browser_name')
    if browser_name.lower() == 'chrome':
        return webdriver.Chrome()
    # elif browser_name.lower() == 'firefox':
    #     return webdriver.Firefox()
    # elif browser_name.lower() == 'edge':
    #     return webdriver.Edge()
    else:
        raise ValueError('Unsupported browser: {}'.format(browser_name))