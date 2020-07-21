# 95. 不同的二叉搜索树 II
# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def generateTrees(self, n):
    def generateTree(tree, mi, ma):
      if mi == ma:
        
    
    def unfoldTree(tree) -> []:




if __name__ == '__main__':
  s = Solution()
  print(s.generateTrees(3))