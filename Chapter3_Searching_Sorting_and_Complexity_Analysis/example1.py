# coding=utf-8
"""
对一个有序列表进行顺序搜索，当目标比列表中给定的元素要小的时候，就可以
停止了。请定义这一算法修改后的版本，并且使用大O表示法，表示其在最好情况、
最差情况和平均情况下的性能。
"""
# best O(1) worst O(n) mean O(n)


def find_func(array, key):
    """
    :param array: sorted list
    :param key: value for find
    :return: the index and value which is lower than key
    """
    for index, value in enumerate(array):
        if key < value:
            return index, value


def main():
    list_ = [i for i in range(5, 10)]
    key = 7
    index, value = find_func(list_, key)
    print("key is {}, value is {}".format(index, value))


if __name__ == '__main__':
    main()
