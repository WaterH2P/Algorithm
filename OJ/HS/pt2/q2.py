class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


for t in range(int(input())):
    n, *arr = input().split()
    n = int(n)
    linked_list = ListNode(arr[0])
    linked_list_ptr = linked_list
    for i in arr[1:]:
        linked_list_ptr.next = ListNode(i)
        linked_list_ptr = linked_list_ptr.next
    linked_list_ptr = linked_list
    flag = list()
    is_palindrome = True
    for i in range(n//2):
        flag.append(linked_list_ptr.val)
        linked_list_ptr = linked_list_ptr.next
    if n % 2:   # 奇数
        linked_list_ptr = linked_list_ptr.next
    for i in range(n//2):
        if linked_list_ptr.val != flag.pop():
            is_palindrome = False
            break
        linked_list_ptr = linked_list_ptr.next
    if is_palindrome:
        print('true')
    else:
        print('false')

