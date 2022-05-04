# -*- encoding: utf-8 -*-
'''
@File    :   sword_010.py
@Time    :   2022/05/04 21:22:03
@Author  :   Dejian Fu
@Version :   1.0
@Contact :   fudejian1008@163.com
'''

# 剑指 Offer II 010. 和为 k 的子数组
# 给定一个整数数组和一个整数 k ，请找到该数组中和为 k 的连续子数组的个数。

# 示例 1：
# 输入:nums = [1,1,1], k = 2
# 输出: 2
# 解释: 此题 [1,1] 与 [1,1] 为两种不同的情况

# 示例 2：
# 输入:nums = [1,2,3], k = 3
# 输出: 2

from typing import List

class Solution:
    # 解法 1， 两层循环，暴力解题
    # 解法 2， 前缀和
    # sums[i+1] 表示 sum(nums[0:i+1])
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = [0]
        for num in nums:
            sums.append(sums[-1] + num)
        print(sums)


sol = Solution()
nums = [1,1,1]
k = 2

nums = [1,2,3]
k = 3

nums = [-1,-1,1]
k = 0

print(sol.subarraySum(nums,k))