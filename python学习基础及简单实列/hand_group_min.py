"""
对数据分组
"""

import csv
import json
import os
import urllib.parse

import xlrd
import xlwt
from xlutils.copy import copy


def read_csv(file_path):
    '''
    读取 csv 数据
    :param file_path:
    :return:
    '''
    file_object = open(file_path, encoding='gbk')
    csv_object = csv.reader(file_object, delimiter="#", quoting=csv.QUOTE_NONE)
    return csv_object


def handle_data(csv_data, line=1000):
    '''
    处理整合数据
    :param csv_data:
    :param line:
    :return:
    '''
    results_values = {}
    i = 0
    for row in csv_data:
        if row[0] == 'uid':
            continue
        if len(row) != 7:
            continue
        uId = row[0]
        row[1] = ua = urllib.parse.unquote(row[1])
        entry = row[2]
        refer = row[3]
        loc = row[4]
        logindatetime = row[5]
        ip = row[6]
        ip_segment = handle_ip(ip, 2)
        compare_value = ua+'#'+entry+'#'+refer+'#'+loc+'#'+logindatetime+'#'+ip_segment

        if compare_value in results_values.keys():
            results_values[compare_value].append(row)
        else:
            results_values[compare_value] = [row]

        i += 1
        if i == line:
            break
    return results_values


def handle_ip(ip, n=2):
    """
    处理 ip
    :param ip:
    :param n:
    :return:
    """
    result = ""
    if n <= 0:
        result = ""
    if n >= 4:
        result = ip
    if (ip != "") and (n > 0) and (n < 4):
        ip_list = ip.split('.', 4)
        result_list = []
        for i in range(0, n):
            result_list.append(ip_list[i])
        result = '.'.join(result_list)
    return result


# 写入 excel
def write_execl(values, file='data.xls', startRow=0):
    """ 写入整合好的数据到文件 """
    if not os.path.isfile(file):
        write = xlwt.Workbook()
        write.add_sheet('data', cell_overwrite_ok=True)
        write.save(file)

    old_data = xlrd.open_workbook(file)
    write = copy(old_data)
    write_sheet = write.get_sheet(0)

    # 列标题
    row_title = ['uid', 'ua', 'entry', 'refer', 'loc', 'logindatetime','ip']

    if startRow is 0:
        for x in range(len(row_title)):
            write_sheet.write(0, x, row_title[x])

    for i in range(len(values)):
        write_sheet.write(startRow + i + 1, 0, values[i][0])
        write_sheet.write(startRow + i + 1, 1, values[i][1])
        write_sheet.write(startRow + i + 1, 2, values[i][2])
        write_sheet.write(startRow + i + 1, 3, values[i][3])
        write_sheet.write(startRow + i + 1, 4, values[i][4])
        write_sheet.write(startRow + i + 1, 5, values[i][5])
        write_sheet.write(startRow + i + 1, 5, values[i][6])
    write.save(file)

if __name__ == '__main__':

    # 读取的csv文件
    file = 'ua_11_011.csv'
    # 保存的文件
    save = 'a_2group.xls'
    # 过滤出现最小次数
    same_number = 30

    data = read_csv(file)
    results_data = handle_data(data, 69000)
    line = 0
    for key, group_value in results_data.items():
        if len(group_value) < same_number:
            continue
        # print(group_value)
        write_execl(group_value, save, line)
        line += len(group_value)
