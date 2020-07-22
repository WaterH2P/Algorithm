# 剑指 Offer 11. 旋转数组的最小数字
# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

class Solution:
  def minArray(self, numbers) -> int:
    def findMin(numbers, l, r):
      if l > r:
        return int('inf')
      elif l + 1 >= r:
        return min(numbers[l], numbers[r])
      else:
        mid = (l + r) // 2
        if numbers[mid - 1] <= numbers[mid] <= numbers[mid + 1]:
          return min(findMin(numbers, l, mid - 1), findMin(numbers, mid + 1, r))
        else:
          return min(numbers[mid - 1], numbers[mid], numbers[mid + 1])
    return findMin(numbers, 0, len(numbers) - 1)

if __name__ == "__main__":
  s = Solution()
  numbers = [3,4,5,6,7,1,2]
  print(s.minArray(numbers))