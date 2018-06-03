# coding=utf-8
"""
TidBit计算机商店有一个针对计算机销售的信用卡计划。这包括一个10%的分期付款
和一个年息12%的利息。每月的付款是销售定价的5%再减去分期付款。编写一个程序，
它接收销售价格作为输入。程序应该显示一个表格，它拥有相应的表头，它包括借贷
的整个还款周期的支付计划。它的每一行应该包括如下项：
1. 第几个月（从1开始）
2. 当月的欠款总额
3. 该月所欠利息
4. 该月所欠本金
5. 该月还款额
6. 在还款之后所欠的总余额
一个月的利息等于余额*利率/12。一个月的本金额等于该月的还款减去所欠的利息。
"""