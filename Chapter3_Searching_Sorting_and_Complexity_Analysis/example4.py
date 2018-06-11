# coding=utf-8
"""
expo函数的一个可替代的策略是，使用如下的递归定义：
expo(number, exponent)
=1, 当exponent=0
=number*expo(number, exponent-1) 当exponent是基数的时候
=(expo(number,exponent/2))^2， 当exponent是偶数的时候
使用这一策略定义一个递归的expo函数，并且使用大O表示法表示其复杂度。
"""
# O(nlogn)


def expo(number, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 1:
        return number * expo(number, exponent - 1)
    else:
        return expo(number, exponent//2) ** 2


def main():
    num = 2
    times = 128
    out = expo(num, times)
    print("{} 的 {} 次幂是：".format(num, times), out)


if __name__ == '__main__':
    main()