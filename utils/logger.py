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
import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)
# 设置将日志输出到文件中，并且定义文件内容
now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
fileinfo = logging.FileHandler(f"logs\\AutoTest_log_{now}.log")
fileinfo.setLevel(logging.INFO)
# 设置将日志输出到控制台
controlshow = logging.StreamHandler()
controlshow.setLevel(logging.INFO)
# 设置日志的格式
formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")
fileinfo.setFormatter(formatter)
controlshow.setFormatter(formatter)

logger.addHandler(fileinfo)
logger.addHandler(controlshow)


def get_logger():
    return logger