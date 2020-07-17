# 543. 二叉树的直径
# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None or (root.left is None and root.right is None):
            return 0
        root.maxh = 0
        def deep(tree: TreeNode, root: TreeNode) -> int:
            tree.lh = deep(tree.left, root) + 1 if tree.left is not None else 0
            tree.rh = deep(tree.right, root) + 1 if tree.right is not None else 0
            if tree.lh + tree.rh > root.maxh:
                root.maxh = tree.lh + tree.rh
            return max(tree.lh, tree.rh)
        deep(root, root)
        return max(root.lh + root.rh, root.maxh)

if __name__ == '__main__':
    s = Solution()

    result = 3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right = TreeNode(3)

    print(s.diameterOfBinaryTree(root))



    result = 1
    root = TreeNode(1)
    root.right = TreeNode(2)

    print(s.diameterOfBinaryTree(root))



    result = 3
    root = TreeNode(4)
    root.left = TreeNode(1)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(3)

    print(s.diameterOfBinaryTree(root))