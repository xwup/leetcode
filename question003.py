'''
给定一个字符串，找出不含有重复字符的 最长子串 的长度。

示例：

给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。

给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。

给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列 而不是子串。
'''


# class Solution:
# def lengthOfLongestSubstring(self, s):
#     """
#     :type s: str
#     :rtype: int
#     """
#
#     if len(s) == 0:
#         return 0
#     maxlong = 0
#     tmp = []
#     for i in range(len(s)):
#         if s[i] in tmp:
#             if len(tmp) > maxlong:
#                 maxlong = len(tmp)
#             pot = tmp.index(s[i]) + 1
#             tmp = tmp[pot:]
#         tmp.append(s[i])
#     if ''.join(tmp) == s:
#         maxlong = len(s)
#     if maxlong < len(tmp):
#         maxlong = len(tmp)
#     return maxlong
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        length = 0
        ans = 0
        for i, c in enumerate(s):
            if c in d and i - d[c] <= length:
                length = i - d[c]
                d[c] = i
            else:
                d[c] = i
                length += 1
            if length > ans: ans = length
            # print(length)
        return ans


if __name__ == '__main__':
    s = "abba"
    maxlong = Solution().lengthOfLongestSubstring(s)
    print(maxlong)
