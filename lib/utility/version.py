#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 此代码仅供学习与交流，请勿用于商业用途。
# 判断Python版本环境


import sys

if sys.version_info < (3, 0):   # 如果小于Python3
    PYTHON_3 = False  # 标记为非Python3环境
else:
    PYTHON_3 = True  # 标记为Python3环境

if not PYTHON_3:   # 如果小于Python3
    from importlib import reload  # 导入reload函数
    reload(sys)  # 重新加载sys模块
    sys.setdefaultencoding("utf-8")  # 设置默认编码为utf-8，解决中文编码问题
