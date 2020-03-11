# 988. 从叶结点开始的最小字符串
# 给定一颗根结点为 root 的二叉树，书中的每个结点都有一个从 0 到 25 的值，分别代表字母 'a' 到 'z'：值 0 代表 'a'，值 1 代表 'b'，依此类推。
# 找出按字典序最小的字符串，该字符串从这棵树的一个叶结点开始，到根结点结束。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# dfs
# class Solution(object):
#     def smallestFromLeaf(self, root):
#         self.ans = "~"

#         def dfs(node, A):
#             if node:
#                 A.append(chr(node.val + ord('a')))
#                 if not node.left and not node.right:
#                     self.ans = min(self.ans, "".join(reversed(A)))
#                 dfs(node.left, A)
#                 dfs(node.right, A)
#                 A.pop()

#         dfs(root, [])
#         return self.ans

# bfs
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        root.parent = None
        minEle = 26
        bfs, leafs, res = [root], [], []
        while len(bfs) > 0:
            ele = bfs.pop(0)
            if ele.left is None and ele.right is None:
                if ele.val < minEle:
                    minEle = ele.val
                    leafs = [ele]
                elif ele.val == minEle:
                    leafs.append(ele)
            if ele.left is not None:
                ele.left.parent = ele
                bfs.append(ele.left)
            if ele.right is not None:
                ele.right.parent = ele
                bfs.append(ele.right)
        for ele in leafs:
            road = ''
            while ele.parent is not None:
                road += chr(ele.val + 97)
                ele = ele.parent
            road += chr(root.val + 97)
            res.append(road)
        res.sort()
        return res[0]

if __name__ == '__main__':
    s = Solution()

    result = 'dba'
    tree = TreeNode(0)
    tree.left = TreeNode(1)
    tree.left.left = TreeNode(3)
    tree.left.right = TreeNode(4)

    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    tree.right.right = TreeNode(4)

    print(s.smallestFromLeaf(tree))


    result = 'adz'
    tree = TreeNode(25)
    tree.left = TreeNode(1)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)

    tree.right = TreeNode(3)
    tree.right.left = TreeNode(0)
    tree.right.right = TreeNode(2)

    print(s.smallestFromLeaf(tree))