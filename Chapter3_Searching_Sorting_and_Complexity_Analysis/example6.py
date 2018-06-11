# coding=utf-8
"""
修改递归的Fibonacci函数，以使用本章前面介绍的记忆（memorization）技术。
该函数应该接收字典作为额外的参数。该函数最顶层的调用，接受一个空的字典。
函数的键和值应该是这个递归调用的参数和值。此外，使用本章讨论的计时器对象
来统计递归调用的次数。
"""
from Chapter3_Searching_Sorting_and_Complexity_Analysis.profiler import Profiler


def fibonacci(dict_, n, profiler):
    if n == 1 or n == 2:
        dict_[n] = 1
    elif n-1 and n-2 in dict_.keys():
        dict_[n] = dict_[n-1] + dict_[n-2]
    elif n-1 in dict_.keys():
        if n-3 and n-4 in dict_.keys():
            dict_[n-2] = dict_[n-3] + dict_[n-4]
        elif n-3 in dict_.keys():
            dict_[n-2] = dict_[n-3] + fibonacci(dict_, n-4, profiler)
        elif n-4 in dict_.keys():
            dict_[n-2] = fibonacci(dict_, n-3, profiler) + dict_[n-4]
        else:
            dict_[n-2] = fibonacci(dict_, n-3, profiler) + fibonacci(dict_, n-4, profiler)
        dict_[n] = dict_[n-1] + dict_[n-2]
    elif n-2 in dict_.keys():
        if n-3 in dict_.keys():
            dict_[n-1] = dict_[n-2] + dict_[n-3]
        else:
            dict_[n-1] = dict_[n-2] + fibonacci(dict_, n-3, profiler)
        dict_[n]=dict_[n - 1] + dict_[n - 2]
    else:
        if n-3 and n-4 in dict_.keys():
            dict_[n-2] = dict_[n-3] + dict_[n-4]
        elif n-3 in dict_.keys():
            dict_[n-2] = dict_[n-3] + fibonacci(dict_, n-4, profiler)
        elif n-4 in dict_.keys():
            dict_[n-2] = fibonacci(dict_, n-3, profiler) + dict_[n-4]
        else:
            dict_[n-2] = fibonacci(dict_, n-3, profiler) + fibonacci(dict_, n-4, profiler)
        dict_[n - 1] = dict_[n-2] + dict_[n-3]
        dict_[n] = dict_[n - 1] + dict_[n - 2]
    return dict_[n]


def main():
    a = {}
    profiler = Profiler()
    key = int(input("Enter key:"))
    value = fibonacci(a, key, profiler)
    print(value)


if __name__ == '__main__':
    main()