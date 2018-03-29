'''
给定一个范围为 32 位 int 的整数，将其颠倒。

例 1:

输入: 123
输出:  321


例 2:

输入: -123
输出: -321


例 3:

输入: 120
输出: 21


注意:

假设我们的环境只能处理 32 位 int 范围内的整数。根据这个假设，如果颠倒后的结果超过这个范围，则返回 0。
'''


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if (x < 0):
            y = -1 * int((str(-x))[::-1])
        else:
            y = int((str(x))[::-1])
        if (y > (2 ** 32 / 2 - 1) or y < (-(2 ** 32 / 2))):
            y = 0
        return (y)

'''
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = -int(str(x)[1:][::-1]) if x < 0 else int(str(x)[::-1])
        return y if -2**31 < y < 2**31 - 1 else 0
'''


if __name__ == '__main__':
    x = 1534236469
    result = Solution().reverse(x)
    print(result)
