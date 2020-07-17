# 1526 面试题33. 二叉搜索树的后序遍历序列
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。
# 假设输入的数组的任意两个数字都互不相同。


# 循环
# class Solution:
#     def verifyPostorder(self, postorder) -> bool:
#         eles = [[_ for _ in postorder]]
#         while len(eles) > 0:
#             index, ele = 0, eles.pop(0)
#             if len(ele) <= 2: continue
#             while index < len(ele) - 1 and ele[index] < ele[-1]:
#                 index += 1
#             if index == len(ele) - 1: eles.append([*ele[:-1]])
#             else:
#                 for item in ele[index:-1]:
#                     if item <= ele[-1]: return False
#                 eles.append([*ele[:index]])
#                 eles.append([*ele[index:-1]])
#         return True

# 递归
class Solution:
    def verifyPostorder(self, postorder) -> bool:
        def verify(order):
            if len(order) <= 2: return True
            index = 0
            while index < len(order) - 1 and order[index] < order[-1]:
                index += 1
            if index == len(order) - 1: return verify([*order[:-1]])
            else:
                for item in order[index:-1]:
                    if item <= order[-1]: return False
                return verify([*order[:index]]) and verify([*order[index:-1]])
        return verify(postorder)


if __name__ == '__main__':
    s = Solution()
    result = False
    postorder = [1,6,3,2,5]
    print(s.verifyPostorder(postorder))

    result = True
    postorder = [1,3,2,6,5]
    print(s.verifyPostorder(postorder))