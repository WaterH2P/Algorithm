class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_link(head: ListNode, k: int) -> ListNode:
    next = None
    prev = None
    for j in range(k):
        print(head.val, j)
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


for t in range(int(input())):
    n, *arr, k = input().split()
    n, k = int(n), int(k)
    linked_list = ListNode(arr[0])
    head = linked_list
    for i in arr[1:]:
        head.next = ListNode(i)
        head = head.next
    start = None
    head = linked_list
    for i in range(n//k):
        head = reverse_link(head, k)
        if i == 0:
            start = head
        for j in range(k):
            head = head.next
    res = list()
    ptr = start
    for i in range(n):
        res.append(ptr.val)
        ptr = ptr.next
    print(*res)



