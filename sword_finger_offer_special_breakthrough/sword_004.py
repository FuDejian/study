# -*- encoding: utf-8 -*-
'''
@File    :   sword_004.py
@Time    :   2022/05/03 22:42:10
@Author  :   Dejian Fu
@Version :   1.0
@Contact :   fu.dejian@foxmail.com
'''

# 剑指 Offer II 004. 只出现一次的数字 
# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

# 示例 1：
# 输入：nums = [2,2,3,2]
# 输出：3

# 示例 2：
# 输入：nums = [0,1,0,1,0,1,100]
# 输出：100

from collections import Counter
from typing import List

class Solution:

    # 方法1， 调用库函数
    # Counter，统计列表中各元素出现的次数
    # 执行用时：32 ms, 在所有 Python3 提交中击败了96.35%的用户
    # 内存消耗：16.1 MB, 在所有 Python3 提交中击败了73.30%的用户
    def singleNumber(self, nums: List[int]) -> int:
        num_cun = Counter(nums)
        for k,v in num_cun.items():
            if v == 1:
                return k
    
    # 方法2， 以此确定每一个二进制位
    # 由于数组中的元素都在int（即32位整数）范围内，因此我们可以依次计算答案的每一个二进制位是0还是1。
    # 具体地，考虑答案的第 i 个二进制位（i 从 0 开始编号），它可能为 0 或 1。对于数组中非答案的元素，
    # 每一个元素都出现了3 次，对应着第 i 个二进制位的 3 个 0 或 3 个 1，无论是哪一种情况，
    # 它们的和都是 3 的倍数（即和为 0 或 3）。因此：
    # 答案的第 i 个二进制位就是数组中所有元素的第 i 个二进制位之和除以 3 的余数。
    # 这样一来，对于数组中的每一个元素 x，我们使用位运算 (x >> i) & 1 得到 x 的第 i 个二进制位，
    # 并将它们相加再对 3 取余，得到的结果一定为 0 或 1，即为答案的第 i 个二进制位。

    # 执行用时：92 ms, 在所有 Python3 提交中击败了29.15%的用户
    # 内存消耗：16 MB, 在所有 Python3 提交中击败了89.82%的用户

    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            total = sum((num>>i)&1 for num in nums)
            if total % 3:
                if i == 31:
                    res -= (1 << i)
                else:
                    res |= (1 << i)
        return res