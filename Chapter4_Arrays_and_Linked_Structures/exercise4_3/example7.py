# coding=utf-8
"""
编写一段代码，使用整数来表示其3个索引位置，从而初始化一个三维数组中的
每一个单元。因此，如果一个位置的形式是（depth，row，column），位于
（2，3，3）的整数数据是233.
"""
from Chapter4_Arrays_and_Linked_Structures.exercise4_3.arrays import Array


def main():
    depth = 4
    row = 4
    col = 4
    arr = Array(depth)
    for i in range(depth):
        arr[i] = Array(row)
    for i in range(depth):
        for j in range(row):
            arr[i][j] = Array(col)
    for i in range(depth):
        for j in range(row):
            for k in range(col):
                arr[i][j][k] = i * 100 + j * 10 + k
    print(arr[2][3][3])


if __name__ == '__main__':
    main()