# 【简单】993. 二叉树的堂兄弟节点
# 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。
# 如果二叉树的两个节点深度相同，但父节点不同，则它们是一对堂兄弟节点。
# 我们给出了具有唯一值的二叉树的根节点 root，以及树中两个不同节点的值 x 和 y。
# 只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true。否则，返回 false。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        a, b, isX, isY = 1, 0, False, False
        eles = [root]
        while len(eles) > 0:
            ele = eles.pop(0)
            a -= 1

            if ele.val == x: isX = True
            if ele.val == y: isY = True
            if ele.left:
                eles.append(ele.left)
                b += 1
            if ele.right:
                eles.append(ele.right)
                b += 1
            if ele.left and ele.right:
                if ele.left.val == x and ele.right.val == y: return False
                if ele.left.val == y and ele.right.val == x: return False
            if a == 0:
                if isX and isY: return True
                if isX or isY: return False
                a, b = b, 0
        return False


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.right = TreeNode(3)
    x, y = 4, 3
    print(s.isCousins(root, x, y))