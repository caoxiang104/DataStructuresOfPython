# coding=utf-8
"""
统计学家想要用一组函数计算一列数字的中位数（median）和众数（mode）。
中位数是将一个列表排序后出现在中间位置的数。众数是在列表中出现最频
繁的数。在名为stats.py的模块中定义这些函数。还要包括一个名为mean
的函数，它计算一组数字的平均数。每个函数都接受一个列表作为参数，并
且返回单个的数字。
"""


class Stats(object):
    def __init__(self, list_):
        list_.sort()
        self.list_ = list_

    def __str__(self):
        return str(self.list_)

    def mean(self):
        return sum(self.list_) / len(self.list_)

    def median(self):
        if len(self.list_) % 2 == 0:
            return (self.list_[len(self.list_)//2] + self.list_[len(self.list_)//2 - 1]) / 2
        else:
            return self.list_[len(self.list_)//2]

    def mode(self):
        sum_ = 1
        max_sum = 1
        index = 0
        temp = self.list_[0]
        for i in range(1, len(self.list_)):
            if self.list_[i] == temp:
                sum_ += 1
            else:
                temp = self.list_[i]
                if sum_ > max_sum:
                    max_sum = sum_
                    index = i - 1
                sum_ = 1
        if sum_ > max_sum:
            index = len(self.list_) - 1
        return self.list_[index]


def main():
    list_num = input("Please enter number:")
    list_ = []
    for i in list_num.split():
        list_.append(int(i))
    stats = Stats(list_)
    print("Mean value of list is:", stats.mean())
    print("Median value of list is:", stats.median())
    print("Mode value of list is:", stats.mode())


if __name__ == '__main__':
    main()







