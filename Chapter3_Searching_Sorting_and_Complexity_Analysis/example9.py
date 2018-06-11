# coding=utf-8
"""
修改quicksort函数，以便其调用插入排序来对规模小于50的子列表进行排序。
分别使用50项，500项和5000项的数据集来比较这个版本和最初版本的性能。然
后，使用插入排序来调整阈值，确定最优化设置。
"""
import random
import time


def insertion_sort(list_):
    n = len(list_)
    i = 1
    while i < n:
        key = list_[i]
        j = i - 1
        while j >= 0 and list_[j] > key:
            list_[j + 1] = list_[j]
            j -= 1
        list_[j + 1] = key
        i += 1
    return list_


def quick_sort(list_, left, right):
    if left < right:
        q = partition(list_, left, right)
        if q - left <= 30:
            insertion_sort(list_[left:q - 1])
        else:
            quick_sort(list_, left, q - 1)
        if right - q <= 30:
            insertion_sort(list_[q + 1:right])
        else:
            quick_sort(list_, q + 1, right)
    return list_


def partition(list_, left, right):
    mid = (left + right) // 2
    list_[mid], list_[right] = list_[right], list_[mid]
    j = left - 1
    key = list_[right]
    for i in range(left, right):
        if list_[i] <= key:
            j += 1
            list_[i], list_[j] = list_[j], list_[i]
    list_[j + 1], list_[right] = list_[right], list_[j + 1]
    return j + 1


def main():
    times = 5000
    list_ = [i for i in range(times)]
    random.shuffle(list_)
    start = time.time()
    insertion_sort(list_)
    finish = time.time() - start
    print("insertion sort for a list of length {} need {} s".format(times, finish))
    random.shuffle(list_)
    start = time.time()
    quick_sort(list_, 0, len(list_) - 1)
    finish = time.time() - start
    print("quick sort for a list of length {} need {} s".format(times, finish))


if __name__ == '__main__':
    main()