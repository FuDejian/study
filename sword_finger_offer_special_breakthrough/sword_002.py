# -*- encoding: utf-8 -*-
'''
@File    :   sword_002.py
@Time    :   2022/05/03 11:39:07
@Author  :   Dejian Fu
@Version :   1.0
@Contact :   fudejian1008@163.com
'''

# 剑指 Offer II 002. 二进制加法
# 给定两个 01 字符串 a 和 b ，请计算它们的和，并以二进制字符串的形式输出。
# 输入为 非空 字符串且只包含数字 1 和 0。

# 示例 1:
# 输入: a = "11", b = "10"
# 输出: "101"

# 示例 2:
# 输入: a = "1010", b = "1011"
# 输出: "10101"

# 解法：
# 分别计算出对应的十进制数字，相加后转换成二进制字符

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]