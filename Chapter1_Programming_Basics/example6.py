# coding=utf-8
"""
工资部门将每个支付周期的雇员信息的列表保存到一个文本文件中。该文件的每一行格式如下：
            <last name><hourly wage><hours worked>
编写一个程序，让用户输入一个文件名并且向终端输入报表，展示在给定的周期应该向每一个雇
员支付的工资。这个报表应该是表格形式，并且具有相应的表头。每一行一个包含雇员的名称、
工作的小时数，以及该周期所支付的工资
"""
import sys
from prettytable import PrettyTable


def build_txt(txt_name):
    f = open(txt_name, 'w')
    f.write("LastName HourlyWage HoursWorked\n")
    s = sys.stdin.readlines()
    for i in s:
        f.write(i)
    f.close()
    return f


def read_txt(txt_name):
    f = open(txt_name, 'r')
    words = []
    contents = f.readlines()
    for line in contents:
        line = line.split()
        words.append(line)
    f.close()
    return words


def cal_pay(words):
    words[0].append("pay")
    for i in range(1, len(words)):
        words[i].append(int(words[i][1]) * int(words[i][2]))
    return words


def main():
    # build_txt("example6.txt")
    words = read_txt("example6.txt")
    words = cal_pay(words)
    for i in range(len(words)):
        if i == 0:
            table = PrettyTable(words[0])
        else:
            table.add_row(words[i])
    print(table)


if __name__ == '__main__':
    main()


