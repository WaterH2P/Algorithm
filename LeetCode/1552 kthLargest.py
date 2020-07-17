# 1552 面试题54. 二叉搜索树的第k大节点。
# 给定一棵二叉搜索树，请找出其中第k大的节点。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.node = None

        def dfs(root: TreeNode):
            if self.k == 0: return None
            if root.right: dfs(root.right)
            self.k -= 1
            if self.k == 0: self.node = root
            if root.left: dfs(root.left)
        
        dfs(root)
        return self.node.val

if __name__ == '__main__':
    s = Solution()

    result = 4
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right = TreeNode(4)

    print(s.kthLargest(root, 1))

    result = 4
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(1)
    root.left.right = TreeNode(4)

    root.right = TreeNode(6)

    print(s.kthLargest(root, 1))
