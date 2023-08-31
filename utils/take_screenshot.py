# -*- coding:utf-8 _*-
# coding=utf-8
"""
@Time: 2023/8/13 14:46
@Auth: 王浩鹏
@File ：take_screenshot.py
"""
import os
from datetime import datetime
from utils.driver import get_driver


def take_screenshot(driver, name):
    # driver = get_driver() 如果使用这个重新获取驱动，截图是空白的
    screenshot_dir = os.path.join(os.path.dirname(__file__), '..\\report\\images')
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_file = os.path.join(screenshot_dir,
                                   '{}_{}.png'.format(name, datetime.now().strftime('%Y-%m-%d_%H-%M-%S')))
    driver.save_screenshot(screenshot_file)