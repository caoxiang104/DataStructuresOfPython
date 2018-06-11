# coding=utf-8
"""
Python的列表方法sort包含了一个关键参数reverse，其默认值为False。程序
员可以覆盖这个值，从而按照降序来对列表排序。修改本章前面介绍的selectionSort
函数，以允许程序员为其提供一个额外的参数来重定向排序。
"""
import random


def selectionSort(list_, reverse=False):
    i = 0
    index = i
    while i < len(list_) - 1:
        j = i + 1
        while j < len(list_):
            if reverse:
                if list_[j] > list_[index]:
                    index = j
            else:
                if list_[j] < list_[index]:
                    index = j
            j += 1
        if index != i:
            list_[i], list_[index] = list_[index], list_[i]
        i += 1
        index = i


def main():
    list_ = [i for i in range(10)]
    random.shuffle(list_)
    selectionSort(list_, True)
    print("list is:", "".join(str(list_)))
    selectionSort(list_, False)
    print("list is:", "".join(str(list_)))


if __name__ == '__main__':
    main()       