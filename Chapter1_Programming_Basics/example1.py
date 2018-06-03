# coding=utf-8
"""
编写一个程序，它以球体的半径（浮点数）作为输入，并且输出球体的直径、圆周长、表面积和体积
"""
from math import pi


def diameter(radius):
    # 直径
    return 2 * radius


def circumference(radius):
    # 圆周长
    return 2 * pi * radius


def surfaceArea(radius):
    # 表面积
    return 4 * pi * radius ** 2


def volume(radius):
    return 4 / 3 * pi * radius ** 3


def main():
    radius = float(input("Please enter radius:"))
    print("Diameter is:", diameter(radius))
    print("circumference of circle is:", circumference(radius))
    print("Surface area of ball is:", surfaceArea(radius))
    print("Volume of ball is:", round(volume(radius), 3))


if __name__ == '__main__':
    main()