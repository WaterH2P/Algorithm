# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root, target, K: int):
        eles = [root]
        root.parent = None
        while len(eles) > 0:
            ele = eles.pop(0)
            if ele.left != None:
                ele.left.parent = ele
                eles.append(ele.left)
            if ele.right != None:
                ele.right.parent = ele
                eles.append(ele.right)
        res, eles = [], [[target, K, True, True, True]]    # parent, left, right
        while len(eles) > 0:
            ele = eles.pop(0)
            if ele[0] != None and ele[1] == 0:
                res.append(ele[0].val)
            else:
                if ele[2] and ele[0].parent:
                    if ele[0].parent.left != None and ele[0].parent.left.val == ele[0].val:
                        eles.append([ele[0].parent, ele[1] - 1, True, False, True])
                    elif ele[0].parent.right != None and ele[0].parent.right.val == ele[0].val:
                        eles.append([ele[0].parent, ele[1] - 1, True, True, False])
                if ele[3] and ele[0].left:
                    eles.append([ele[0].left, ele[1] - 1, False, True, True])
                if ele[4] and ele[0].right:
                    eles.append([ele[0].right, ele[1] - 1, False, True, True])
        return res

s = Solution()

root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

target = root.left
dis = 2

print( s.distanceK(root, target, dis) )



root = TreeNode(0)
root.right = TreeNode(1)
root.right.right = TreeNode(2)
root.right.right.right = TreeNode(3)

target = root.right
dis = 2

print( s.distanceK(root, target, dis) )



root = TreeNode(0)
root.left = TreeNode(2)

root.right = TreeNode(1)
root.right.right = TreeNode(3)

target = root.right.right
dis = 3

print( s.distanceK(root, target, dis) )



root = TreeNode(0)
root.left = TreeNode(1)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)
root.left.right.right.right = TreeNode(4)

target = root.left.right.right
dis = 0

print( s.distanceK(root, target, dis) )