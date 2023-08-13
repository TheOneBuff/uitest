# -*- coding:utf-8 _*-
# coding=utf-8
"""
@Time: 2023/8/13 14:44
@Auth: 王浩鹏
@File ：read_config.py.py
"""
import os
from configparser import ConfigParser

config = ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '../config/config.ini'))


def get_base_url():
    return config.get('URL', 'base_url')