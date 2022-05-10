# -*- encoding: utf-8 -*-
'''
@File    :   sword_003.py
@Time    :   2022/05/03 16:22:40
@Author  :   Dejian Fu
@Version :   1.0
@Contact :   fu.dejian@foxmail.com
'''

# 剑指 Offer II 003. 前 n 个数字二进制中 1 的个数
# 给定一个非负整数 n ，请计算 0 到 n 之间的每个数字的二进制表示中 1 的个数，并输出一个数组。

# 示例 1:
# 输入: n = 2
# 输出: [0,1,1]
# 解释: 
# 0 --> 0
# 1 --> 1
# 2 --> 10

# 示例 2:
# 输入: n = 5
# 输出: [0,1,1,2,1,2]
# 解释:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

from typing import List

class Solution:
    # 解法 1
    # 将每个数转为二进制字符串，再将每一位转为列表，最后求和
    # 执行用时：240 ms, 在所有 Python3 提交中击败了5.08%的用户
    # 内存消耗：15.9 MB, 在所有 Python3 提交中击败了87.32%的用户
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            tmp = bin(i)
            cnt = sum([int(j) for j in tmp[2:]])
            res.append(cnt)
        return res

    # 解法 2. Brian Kernighan 算法
    # x&(x-1) 可以去除x的最后一个1
    # 将x&(x-1) 赋值给x,并重复x&(x-1), 直到x为0， 重复次数即为x中1的个数
    # 执行用时：92 ms, 在所有 Python3 提交中击败了22.84%的用户
    # 内存消耗：16 MB, 在所有 Python3 提交中击败了58.80%的用户
    def countBits_2(self, n: int) -> List[int]:
        def count_ones(x):
            res = 0
            while x>0:
                x &= x-1
                res += 1
            return res
        return [count_ones(i) for i in range(n+1)]

    # 解法 3
    # 如果 i&(i-1)=0, 则令high=i，更新当前的最高有效位。
    # i 比 i−highBit 的「一比特数」多1，由于是从小到大遍历每个整数，因此遍历到i时，
    # i−highBit 的「一比特数」已知，令res[i]=res[i−high]+1。
    # 执行用时：48 ms, 在所有 Python3 提交中击败了74.89%的用户
    # 内存消耗：16 MB, 在所有 Python3 提交中击败了45.94%的用户
    def countBits(self, n: int) -> List[int]:
        res = [0]
        high = 0
        for i in range(1, n+1):
            if i & (i-1) == 0:
                high = i
            res.append(res[i-high] + 1)
        return res


    