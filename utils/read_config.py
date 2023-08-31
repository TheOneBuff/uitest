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
config.read(os.path.join(os.path.dirname(__file__), '..\\config\\config.ini'))


def get_base_url():
    return config.get('URL', 'base_url')

# 脑图新增知识点
def get_edit_url():
    return config.get('URL', 'edit_point_url')


def post_update_url():
    return config.get('URL', 'post_update_url')


def get_nodeId_url():
    return config.get('URL', 'get_nodeId_url')


def get_pointview_url():
    return config.get('URL', 'point_view_url')