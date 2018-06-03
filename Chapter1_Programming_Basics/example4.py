# coding=utf-8
"""
德国数学家Gottfried Leibniz为求取π的近似值开发了如下方法：
      π/4 = 1 - 1/3 + 1/5 - 1/7 + ...
编写一个程序，让用户指定在这种近似方法中使用迭代的次数，并且显示最终的结果。
"""


def pi(times):
    sum_ = 0
    for i in range(times):
        temp = 2 * i + 1
        if i % 2 == 0:
            sign = 1
        else:
            sign = -1
        sum_ += sign / temp
    return 4 * sum_


def main():
    times = int(input("Please enter times:"))
    print("The approximate values of π is:", pi(times))


if __name__ == '__main__':
    main()