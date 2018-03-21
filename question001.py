'''
给定一个整数数列，找出其中和为特定值的那两个数。

你可以假设每个输入都只会有一种答案，同样的元素不能被重用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            if target - nums[i] in nums[i + 1:]:
                return [i, nums[i + 1:].index(target - nums[i]) + i + 1]
        return "no answer"


if __name__ == '__main__':
    nums = [3, 3]
    target = 6
    cc = Solution()
    a = cc.twoSum(nums, target)
    print(a)

'''
例子：
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)<=1:
            return(False)
        present = {}
        for i in range(len(nums)):
            if nums[i] in present:
                return(i,present[nums[i]])
            else:
                present[target-nums[i]] = i  
'''