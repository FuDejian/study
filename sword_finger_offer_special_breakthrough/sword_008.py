# -*- encoding: utf-8 -*-
'''
@File    :   sword_008.py
@Time    :   2022/05/04 14:46:10
@Author  :   Dejian Fu
@Version :   1.0
@Contact :   fudejian1008@163.com
'''

# 剑指 Offer II 008. 和大于等于 target 的最短子数组
# 给定一个含有 n 个正整数的数组和一个正整数 target 。
# 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

# 示例 1：
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。

# 示例 2：
# 输入：target = 4, nums = [1,4,4]
# 输出：1

# 示例 3：
# 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
# 输出：0

from typing import List
class Solution:

    # 思路：
    # 双指针滑动窗口， 并求出窗口内数字和大于等于target时长度最小值
    # 当窗口内数组和小于target时，right++
    # 当窗口内数组和大于等于target时，left++
    
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = total = 0
        res = float('inf')
        for right, num in enumerate(nums):
            total += num
            while total >= target:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1
        return res if res <= len(nums) else 0

sol = Solution()
target = 213
nums = [12,28,83,4,25,26,25,2,25,25,25,12]

target = 7
nums = [2,3,1,2,4,3]
print(sol.minSubArrayLen(target, nums))