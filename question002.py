'''
给定两个非空链表来代表两个非负数，位数按照逆序方式存储，它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if len(l1) == 0 or len(l2) == 0:
            return False
        l1 = int(''.join([str(i) for i in list(reversed(l1))]))
        l2 = int(''.join([str(i) for i in list(reversed(l2))]))

        l3 = l1 + l2
        l3 = [int(i) for i in list(reversed(str(l3)))]
        return l3


if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    ss = Solution()
    l3 = ss.addTwoNumbers(l1, l2)
    print(l3)
