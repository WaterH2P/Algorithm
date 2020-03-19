
# 【中等】144. 二叉树的前序遍历
# 给定一个二叉树，返回它的 前序 遍历。
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode):
        if not root: return []
        eles, res = [root], []
        while eles:
            ele = eles.pop()
            res.append(ele.val)
            if ele.right: eles.append(ele.right)
            if ele.left: eles.append(ele.left)
        return res


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(s.preorderTraversal(root))