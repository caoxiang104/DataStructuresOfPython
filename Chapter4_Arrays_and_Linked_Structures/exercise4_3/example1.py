# coding=utf-8
"""
编写一个二维数组或者网格
"""
from Chapter4_Arrays_and_Linked_Structures.exercise4_3.grid import Grid
import numpy as np


def main():
    print("example 1:")
    a = Grid(3, 4)
    for row in range(a.get_height()):
        for col in range(a.get_width()):
            a[row][col] = row * (a.get_height() + 1) + col
    print(a)
    print("example 2:")
    b = np.zeros([3, 4], dtype=np.int)
    print(b)
    m, n = b.shape
    for i in range(m):
        for j in range(n):
            b[i][j] = i * (m + 1) +j
    print(b)


if __name__ == '__main__':
    main()