# -*- coding:utf-8 _*-
# coding=utf-8
"""
@Time: 2023/8/13 14:44
@Auth: 王浩鹏
@File ：logger.py.py
"""
import os
from loguru import logger
from configparser import ConfigParser

config = ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '../config/logger.ini'))

logger.add(config.get('handler_fileHandler', 'class'), level=config.get('logger_root', 'level'),
           rotation=config.getint('handler_fileHandler', 'args')[2],
           retention=config.getint('handler_fileHandler', 'args')[3])


def get_logger(name):
    return logger.bind(name=name)