#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 下午3:48
# @Author  : jaingtao.zhu
# @File    : 基础.py
'''
接口文档
从0到1 搭建接口自动化测试
ID  模块名称  前提条件  接口地址  请求数据   预期结果  实际结果

接口地址 请求数据 接口类型  响应结果
cookie 保存登录状态
seesion   cookie 保存session


header
数据依赖 解决的方案

接口测试用例模版
ID  模块名称  前提条件  接口地址 是否携带header 数据依赖 请求数据   预期结果  实际结果


====================================================
python 操作excel  安装模块  pip3 install xlrd   xutils

data=xlrd.open_workbook('../dataconfig/case1.xls')
tables=data.sheets()[0]

print(tables.nrows)
print(tables.cell_value(2,3))
===========================================
学习操作json数据
请求数据封装成json的格式






















































'''