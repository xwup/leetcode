'''
给定两个非空链表来代表两个非负数，位数按照逆序方式存储，它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        tmp = ans
        tmpsum = 0
        while True:
            if l1 != None:
                tmpsum += l1.val
                l1 = l1.next
            if l2 != None:
                tmpsum += l2.val
                l2 = l2.next
            tmp.val = tmpsum % 10
            tmpsum = tmpsum // 10
            if l1 == None and l2 == None and tmpsum == 0:
                break
            tmp.next = ListNode(0)
            tmp = tmp.next
        return ans


if __name__ == '__main__':
    l1 = ListNode(5)
    l2 = ListNode(5)
    ss = Solution()
    l3 = ss.addTwoNumbers(l1, l2)
    print(l3.val)
