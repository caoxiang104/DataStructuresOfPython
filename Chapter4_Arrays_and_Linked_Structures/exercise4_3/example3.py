# coding=utf-8
"""
编写一段代码，在Grid对象中搜索一个负整数。当在网络第一次找到一个负整
数的时候，循环就应该终止，并且变量row和column应该显示该整数的位置。否
则的话，变量中row和column应该等于网格中的行或者列。
"""
from Chapter4_Arrays_and_Linked_Structures.exercise4_3.grid import Grid


def print_(arr):
    i, j = 0, 0
    for i in range(arr.get_height()):
        for j in range(arr.get_width()):
            if arr[i][j] < 0:
                print("row is {}, col is {}".format(i, j))
                return 0
    print("row is {}, col is {}".format(i, j))
    return 0


def main():
    arr = Grid(4, 4)
    for i in range(arr.get_height()):
        for j in range(arr.get_width()):
            arr[i][j] = i * (arr.get_height() + 1) + j
    arr[2][2] = - 1
    print_(arr)


if __name__ == '__main__':
    main()

