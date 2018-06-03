# coding=utf-8
"""
一个雇员一周的总薪水，等于其每小时的薪水乘以一周正常工作的小时数，
再加上加班费。加班费等于总的加班时间乘以每小时薪水的1.5倍。编写
一个程序，以每小时的薪水，总的常规工作时间和总的加班时间作为参数，
并且显示一个雇员的总周薪。
"""


def weeklyWage(regular_time, overtime, hour_wage):
    return regular_time * hour_wage + 1.5 * overtime * hour_wage


def main():
    regular_time, overtime, hour_wage = map(int, input("Please enter regular time, overtime and hour wage:").split(' '))
    print("The weekly wage is:", weeklyWage(regular_time, overtime, hour_wage))


if __name__ == '__main__':
    main()