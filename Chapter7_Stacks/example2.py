# coding=utf-8
"""
编写一个程序，使用一个栈来测试输入字符串，判断它们是否是回文。
回文是一个单词序列，按照相反的顺序读它的话，内容也是相同的。例如，noon。
"""
from Chapter7_Stacks.linkedstack import LinkedStack


def main():
    ch = input("Please enter a string:")
    stack = LinkedStack()
    for i in ch:
        if stack.isEmpty() or stack.peek() != i:
            stack.push(i)
        else:
            stack.pop()
    if stack.isEmpty():
        print("{} is a Palindrome string.".format(ch))
    else:
        print("{} is not a Palindrome string.".format(ch))


if __name__ == '__main__':
    main()