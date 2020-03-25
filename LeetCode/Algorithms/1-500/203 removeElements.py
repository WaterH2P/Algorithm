# 【简单】203. 移除链表元素
# 删除链表中等于给定值 val 的所有节点。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val: head = head.next
        if not head: return head
        ele = head
        while ele and ele.next:
            if ele.next.val == val: ele.next = ele.next.next
            else: ele = ele.next
        return head