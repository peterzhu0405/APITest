#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 下午3:59
# @Author  : jaingtao.zhu
# @File    : operation_excel.py
import xlrd
from xlutils.copy import copy

'''
操作excel 工具类


'''


class OperationExcel:
    # 初始化数据
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id

        else:
            self.file_name = "../dataconfig/case1.xls"
            self.sheet_id = 0
        self.data = self.get_data()

    # 获取指定表中的数据
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

        # 获取单元格的行数

    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取某一个单元格的内容
    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)

    # 写入数据
    def write_value(self, row, col, value):
        '''
        写入excel数据
        row,col,value
        '''
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)

    # 根据对应的caseid 找到对应行的内容
    def get_rows_data(self, case_id):
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data

    def get_row_values(self, row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data




if __name__ == '__main__':
    opers = OperationExcel()
    print(opers.get_cell_value(1, 2))
    pass
