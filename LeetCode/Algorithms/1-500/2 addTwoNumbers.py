# 【中等】2. 两数相加
# https://leetcode-cn.com/problems/add-two-numbers/
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        temp = res
        isCarry = False
        while l1 != None and l2!= None:
            val = l1.val + l2.val
            if isCarry:
                val += 1
                isCarry = False
            if val >= 10:
                isCarry = True
                val -= 10
            temp.next = ListNode(val)
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        t3 = l1 if l1 != None else l2
        while t3 != None:
            val = t3.val
            if isCarry:
                val += 1
                isCarry = False
            if val >= 10:
                isCarry = True
                val -= 10
            temp.next = ListNode(val)
            temp = temp.next
            t3 = t3.next
        if isCarry:
            temp.next = ListNode(1)
        return res.next

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    s = Solution()
    res = s.addTwoNumbers(l1, l2)
    temp = res
    while temp != None:
        print(temp.val, end=" -> ")
        temp = temp.next
    print()