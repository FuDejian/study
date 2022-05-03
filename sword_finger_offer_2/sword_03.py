# -*- encoding: utf-8 -*-
'''
@File    :   sword_03.py 数组中重复的数字
@Time    :   2022/04/26 22:19:00
@Author  :   Dejian Fu
@Version :   1.0
@Contact :   fudejian1008@163.com
'''

# 剑指 Offer 03. 数组中重复的数字
# 找出数组中重复的数字。
# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
# 数组中某些数字是重复的，但不知道有几个数字重复了，
# 也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。


# 思路：
# 维护一个集合，遍历nums, 
# 当nums中的数字不在集合中时，将数字加入集合
# 反之则是重复数字，直接返回


from typing import List

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        ergodiced = set()
        for num in nums:
            if num in ergodiced:
                ergodiced.add(num)
            else:
                return num