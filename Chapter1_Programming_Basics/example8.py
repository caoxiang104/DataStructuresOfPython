# coding=utf-8
"""
编写一个程序，它允许用户在文件的文本行中导航。程序提示用户输入一个文件名，
并且输入想要放入到列表中的文本行。然后，程序进入到循环中，它会输出文件的行
数，并且提示用户输入一个行号。实际的行号范围是从1到文件的行数。如果用户的输
入是0，程序退出。否则，程序输出和该行号相关的行。
"""
import sys


def file_write(filename):
    f = open(filename, 'w')
    print("Please enter lines which will save in file:")
    lines = sys.stdin.readlines()
    for line in lines:
        f.write(line)
    return f


def file_print(filename):
    num = 1
    f = open(filename, 'r')
    lines = f.readlines()
    while num:
        line_num = int(input("Please enter a number in the range 1~{}:".format(len(lines))))
        if line_num != 0:
            print(lines[line_num - 1])
        else:
            break
    f.close()
    return f


def main():
    filename = input("Please enter filename:")
    # file_write(filename)
    file_print(filename)


if __name__ == '__main__':
    main()