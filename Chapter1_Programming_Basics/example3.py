# coding=utf-8
"""
一个标准的科学家实验是，抛球并且看它能够弹跳多高。一旦球的“弹跳性”已经
确定了，这个比率值就会给出弹跳性的指数。例如：如果球从10高落下调到6米高，
这个索引就是0.6，并且球在一次弹跳后的运动距离是16米。如果球继续弹跳，两
次弹跳后的距离将是10米+6米+3.6米=25.6米。注意，每次后续的弹跳运动的距
离，都是到地板的距离加上这个距离的0.6倍，这个0.6倍就是球反弹回来的距离。
编写一个程序，让用户输入球的一个初始高度以及允许球持续弹跳的次数。输出应
该是球所运动的总距离
"""


def distance(height, times, index=0.6):
    sum_ = 0
    for i in range(times):
        sum_ += height + height * index
        height = height * index
    return sum_


def main():
    height, times = map(int, input("Please enter height and times:").split(' '))
    print("The distance of ball's movement is:", distance(height, times))


if __name__ == '__main__':
    main()
