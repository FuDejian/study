# -*- encoding: utf-8 -*-
'''
@File    :   sword_011.py
@Time    :   2022/05/04 22:44:38
@Author  :   Dejian Fu
@Version :   1.0
@Contact :   fudejian1008@163.com
'''

# 剑指 Offer II 011. 0 和 1 个数相同的子数组
# 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。

# 示例 1：
# 输入: nums = [0,1]
# 输出: 2
# 说明: [0, 1] 是具有相同数量 0 和 1 的最长连续子数组。

# 示例 2：
# 输入: nums = [0,1,0]
# 输出: 2
# 说明: [0, 1] (或 [1, 0]) 是具有相同数量 0 和 1 的最长连续子数组。

from typing import List

class Solution:

    # 思路
    # 遍历nums, 并不断更新此时已经遍历的数字中0和1的个数
    # 遍历dict, key为此时0的个数，并将此时1的个数add到val中
    #   遍历此时的dict, 求此时delta_0, 并判断cnt_1-delta_0是否在val中，
    #   若在，则更新val
    # 结果：超时
    def findMaxLength(self, nums: List[int]) -> int:
        dict = {0:set([0])}
        cnt_0 = cnt_1 = 0
        res = 0
        for num in nums:
            if num == 0:
                cnt_0 += 1
                dict[cnt_0] = set([cnt_1])
            else:
                cnt_1 += 1
                dict[cnt_0].add(cnt_1)
            
            for k, v in dict.items():
                delta_0 = cnt_0 - k
                if cnt_1 - delta_0 in v:
                    res = max(res, 2*delta_0)
        return res

    # 解题
    # 将“0”换为“-1”， 则题目变为求和为0的最长连续子序列长度
    # 用前缀和求解，参考第10题
    def findMaxLength(self, nums: List[int]) -> int:
        res = pre_sum= 0
        dict = {0:-1} # 第一次出现和为key的位置， val为所在索引
        for i, num  in enumerate(nums):
            pre_sum += 1 if num == 1 else -1
            if pre_sum not in dict:
                dict[pre_sum] = i
            else:
                res = max(res, i - dict[pre_sum])
        return res 
            
sol = Solution()
nums = [0,1]
# nums = [1,0,1,1,1,0,0,1,0]
print(sol.findMaxLength(nums))