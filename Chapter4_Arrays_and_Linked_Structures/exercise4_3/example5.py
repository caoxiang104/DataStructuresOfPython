"""
编写一段代码，创建一个杂乱的网络，其行分别包含了3个项、6个项和8个项
"""
from Chapter4_Arrays_and_Linked_Structures.exercise4_3.arrays import Array


def main():
    a = Array(3)
    a[0] = Array(3)
    a[1] = Array(6)
    a[2] = Array(8)
    for i in range(3):
        for j in range(len(a[i])):
            print(a[i][j], end=" ")
        print("")


if __name__ == '__main__':
    main()