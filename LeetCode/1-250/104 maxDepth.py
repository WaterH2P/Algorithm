# -*- coding: UTF-8 -*-
# 104. 二叉树的最大深度
# 给定一个二叉树，找出其最大深度。
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 说明: 叶子节点是指没有子节点的节点。

class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  def maxDepth(self, root: TreeNode) -> int:
    return 0 if not root else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

if __name__ == "__main__":
  s = Solution()
  root = TreeNode(3)
  root.left = TreeNode(9)

  root.right = TreeNode(20)
  root.right.left = TreeNode(15)
  root.right.right = TreeNode(7)

  print(s.maxDepth(root))
