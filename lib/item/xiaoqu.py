#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 此代码仅供学习与交流，请勿用于商业用途。
# 小区信息的数据结构

import sys
from lib.utility.version import PYTHON_3

class XiaoQu(object):
    """
    小区信息类，存储小区名称、区域、价格等信息
    """
    def __init__(self, district, area, name, price, on_sale):
        """
        初始化小区信息
        :param district: 区县
        :param area: 板块
        :param name: 小区名称
        :param price: 价格
        :param on_sale: 在售数量
        """
        self.district = district  # 区县
        self.area = area  # 板块
        self.price = price  # 价格
        self.name = name  # 小区名称
        self.on_sale = on_sale  # 在售数量
    
    def text(self):
        """
        返回小区信息的文本表示，用于写入CSV文件
        :return: 小区信息的文本表示
        """
        return self.district + "," + \
                self.area + "," + \
                self.name + "," + \
                self.price + "," + \
                self.on_sale
