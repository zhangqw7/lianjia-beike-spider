#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 此代码仅供学习与交流，请勿用于商业用途。
# 保存结果到文件

from lib.utility.path import *


def write_urls_to_file(file_name, urls):
    """
    将URL列表写入文件
    :param file_name: 文件名
    :param urls: URL列表
    :return: None
    """
    file_name = DATA_PATH + "/" + file_name  # 构建完整的文件路径
    txt_file = open(file_name, 'w')  # 以写模式打开文件
    for url in urls:  # 遍历URL列表
        txt_file.write(url+"\n")  # 写入URL并换行
    txt_file.close()  # 关闭文件
