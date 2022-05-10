# -*- encoding: utf-8 -*-
'''
@File    :   sword_007.py
@Time    :   2022/05/04 13:37:14
@Author  :   Dejian Fu
@Version :   1.0
@Contact :   fu.dejian@foxmail.com
'''

# 剑指 Offer II 007. 数组中和为 0 的三个数
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a ，b ，c ，使得 a + b + c = 0 ？请找出所有和为 0 且 不重复 的三元组。

# 示例 1：
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]

# 示例 2：
# 输入：nums = []
# 输出：[]

# 示例 3：
# 输入：nums = [0]
# 输出：[]

from typing import List

class Solution:
    # 解法
    # 三数之和转为二数之和
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        res_set = []
        for i, num in enumerate(nums):
            if num > 0 or (i>0 and num == nums[i-1]):
                continue
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[j] + nums[k] + num < 0:
                    j += 1
                elif nums[j] + nums[k] + num > 0:
                    k -= 1
                else:
                    tmp = [nums[i],nums[j],nums[k]]
                    if set(tmp) not in res_set:
                        res_set.append(set(tmp))
                        res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
        return res
    
    # 优化
    # 优化去重部分
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i, num in enumerate(nums[:-2]):
            if num > 0 or (i>0 and num == nums[i-1]):
                continue
            ll, rr = i+1, n-1
            target = -num
            while ll < rr:
                summ = nums[ll] + nums[rr]
                if summ == target:
                    res.append([nums[i],nums[ll],nums[rr]])
                    while ll < rr:
                        ll+=1
                        if nums[ll]!= nums[ll-1]:
                            break
                    while ll < rr:
                        rr-=1
                        if nums[rr]!= nums[rr+1]:
                            break
                elif summ < target:
                    ll += 1
                else:
                    rr -= 1
        return res
sol = Solution()
nums = [-1,0,1,2,-1,-4]
nums = [-4,-1,-1,0,1,2]
nums = [0,0,0,0]
nums = [-2,0,1,1,2]
print(sol.threeSum(nums))