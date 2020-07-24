# -*- coding: UTF-8 -*-
# 117. 填充每个节点的下一个右侧节点指针 II

class Node:
  def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
    self.val = val
    self.left = left
    self.right = right
    self.next = next

class Solution:
  def connect(self, root: 'Node') -> 'Node':
    if not root: return root
    now, pre, first = root, root, root
    isFindNextFirst = False
    now.next = None
    while True:
      # 找到下一行第一个
      if isFindNextFirst:
        if now.left or now.right:
          pre = now
          now = now.left or now.right
          first, isFindNextFirst = now, False
        else: now = now.next
        if not now: break
      else:
        if now == pre.left and pre.right:
          now.next = pre.right
          now = now.next
        elif pre.next:
          now.next, pre = pre.next.left or pre.next.right, pre.next
          if now.next: now = now.next
        else:
          now, isFindNextFirst = first, True
    return root

if __name__ == "__main__":
  s = Solution()

  root = Node(1)
  root.left = Node(2)
  root.left.left = Node(4)
  root.left.right = Node(5)
  root.left.left.left = Node(7)

  root.right = Node(3)
  root.right.right = Node(6)
  root.right.right.right = Node(8)

  def arrTree(root: 'Node'):
    arr = [root]
    index = 0
    while index < len(arr):
      if arr[index].left: arr.append(arr[index].left)
      if arr[index].right: arr.append(arr[index].right)
      index += 1
    return [str(node.val) + ' -> ' + (str(node.next.val) if node.next else 'None') if node != '#' else node for node in arr]
  print(arrTree(s.connect(root)))