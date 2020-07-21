# 865. 具有所有最深结点的最小子树
# 给定一个根为 root 的二叉树，每个结点的深度是它到根的最短距离。
# 如果一个结点在整个树的任意结点之间具有最大的深度，则该结点是最深的。
# 一个结点的子树是该结点加上它的所有后代的集合。
# 返回能满足“以该结点为根的子树中包含所有最深的结点”这一条件的具有最大深度的结点。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.res = []

        def dfs(tree, rank):
            rank.append(tree)
            if tree.left is None and tree.right is None:
                if len(self.res) == 0 or len(rank) > len(self.res[0]):
                    self.res = [[*rank]]
                elif len(rank) == len(self.res[0]):
                    self.res.append([*rank])
            if tree.left is not None:
                dfs(tree.left, [*rank])
            if tree.right is not None:
                dfs(tree.right, [*rank])
        
        dfs(root, [])
        for i in range(len(self.res[0])):
            for j in range(1, len(self.res)):
                if self.res[j][i].val != self.res[0][i].val:
                    return self.res[0][i-1]
        return self.res[0][-1]

if __name__ == "__main__":
    s = Solution()

    tree = TreeNode(3)
    tree.left = TreeNode(5)
    tree.left.left = TreeNode(6)
    tree.left.right = TreeNode(2)
    tree.left.right.left = TreeNode(7)
    tree.left.right.right = TreeNode(4)

    tree.right = TreeNode(1)
    tree.right.left = TreeNode(0)
    tree.right.right = TreeNode(8)

    print(s.subtreeWithAllDeepest(tree))