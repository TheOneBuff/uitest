# -*- coding:utf-8 _*-
# coding=utf-8
"""
@Time: 2023/8/13 14:44
@Auth: 王浩鹏
@File ：logger.py.py
"""
import logging
import os
from loguru import logger
from configparser import ConfigParser

config = ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '..\\config\\logger.ini'))

# logger.add(config.get('handler_fileHandler', 'class'), level=config.get('logger_root', 'level'),
#            rotation='D',retention='')
logging.basicConfig(filename='logs\\test.log')

def get_logger(name):
    return logger.bind(name=name)