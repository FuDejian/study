# -*- encoding: utf-8 -*-
'''
@File    :   leetcode_42.py
@Time    :   2022/04/25 22:14:32
@Author  :   Dejian Fu
@Version :   1.0
@Contact :   fudejian1008@163.com
'''

# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 示例1
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 
# 示例2
# 输入：height = [4,2,0,3,2,5]
# 输出：9


# 第一步，假设最右侧的柱子最高，找到当前柱子处水位高度
# 第二步，假设最左侧的柱子最高，找到当前柱子处水位高度
# 第三步，取1，2中各个柱子处水位较小值，为当前柱子处实际水位
# 第四步，实际水位求和 减去 柱子高度求和，得到答案


from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        height_left, height_right = [height[0]], [height[-1]]

        for h in height[1:]:
            height_left.append(max(height_left[-1], h))

        for h in height[-2::-1]:
            height_right.append(max(height_right[-1], h))
        height_right = height_right[::-1]

        water_h = [min(a,b) for a, b in zip(height_left, height_right)]
        return (sum(water_h) - sum(height))


sol = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.trap(height))
