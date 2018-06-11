# coding=utf-8
"""
列表方法reverse会将列表中的元素反向。定义一个名未reverse的函数，将其
列表参数中的元素反向（不要使用列表中的reverse方法）。尝试让这个方法尽
可能的高效。并且使用大O表示法来表示其复杂度。
"""
# O(n)


def reverse(list_):
    n = len(list_)
    for i in range(0, n//2):
        list_[i], list_[n - 1 - i] = list_[n - 1 - i], list_[i]


def main():
    list_ = [i for i in range(9)]
    reverse(list_)
    print("list is :", "".join(str(list_)))


if __name__ == '__main__':
    main()