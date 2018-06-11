# coding=utf-8
"""
Python的pow函数返回了计算一个数的给定指数所得到的结果。定义一个expo函数
来执行这个任务，并且使用大O表示法来表示其复杂度。该函数的第一个参数是数字，
第二个参数时指数（只能是非负的数字）。在你的实现中，可以使用循环或递归函数。
"""
# O(n)


def expo(num, times):
    if times == 0:
        return 1
    else:
        return num * expo(num, times - 1)


def main():
    num = 2
    times = 5
    out = expo(num, times)
    print("{} 的 {} 次幂是：".format(num, times), out)


if __name__ == '__main__':
    main()