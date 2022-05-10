# -*- encoding: utf-8 -*-
'''
@File    :   sword_005.py
@Time    :   2022/05/04 11:09:38
@Author  :   Dejian Fu
@Version :   1.0
@Contact :   fu.dejian@foxmail.com
'''

# 剑指 Offer II 005. 单词长度的最大乘积
# 给定一个字符串数组 words，请计算当两个字符串 words[i] 和 words[j] 不包含相同字符时，
# 它们长度的乘积的最大值。假设字符串中只包含英语的小写字母。
# 如果没有不包含相同字符的一对字符串，返回 0。

# 示例 1:
# 输入: words = ["abcw","baz","foo","bar","fxyz","abcdef"]
# 输出: 16 
# 解释: 这两个单词为 "abcw", "fxyz"。它们不包含相同字符，且长度的乘积最大。

# 示例 2:
# 输入: words = ["a","ab","abc","d","cd","bcd","abcd"]
# 输出: 4 
# 解释: 这两个单词为 "ab", "cd"。

# 示例 3:
# 输入: words = ["a","aa","aaa","aaaa"]
# 输出: 0 
# 解释: 不存在这样的两个单词。

from typing import List
from collections import namedtuple

class Solution:
    # 解法
    # 将word转换为数字，数字的二进制位分别对应字母‘z~a’,有该字母则该位置1，反之置0
    # 两个word有公共数字则求“&”后结果非零
    # word1.bin & word2.bin == 0 时更新结果
    # 执行用时：404 ms, 在所有 Python3 提交中击败了62.03%的用户
    # 内存消耗：15.6 MB, 在所有 Python3 提交中击败了18.16%的用户

    def maxProduct(self, words: List[str]) -> int:
        wordinfo = namedtuple("wordinfo","word length bin")
        words_info = []
        for word in words:
            tmp = 0
            for i in set(word):
                tmp += 1 << (ord(i) - (ord('a')))
            words_info.append(
                wordinfo(
                    word=word,
                    length=len(word),
                    bin=tmp))
        res = 0
        for i, word1 in enumerate(words_info[:-1]):
            for j, word2 in enumerate(words_info[i+1:]):
                if not word1.bin & word2.bin:
                    res = max(res, word1.length*word2.length)
        return res


sol = Solution()
words = ["abcw","baz","foo","bar","fxyz","abcdef"]
words = ["a","ab","abc","d","cd","bcd","abcd"]
words = ["a","aa","aaa","aaaa"]
print(sol.maxProduct(words))
