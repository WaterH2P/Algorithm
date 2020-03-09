class Solution:
    def totalFruit(self, tree) -> int:
        fruitNum = len(tree)
        if fruitNum <= 2:
            return fruitNum
        maxTotal, total = 0, 1
        fruits = [[tree[0], 0, 0], [-1, -1, -1]]
        for i in range(1, fruitNum):
            if tree[i] == fruits[0][0]:
                if i != fruits[0][2] + 1:
                    fruits[0][1] = i
                fruits[0][2] = i
                total += 1
            elif tree[i] == fruits[1][0]:
                if i != fruits[1][2] + 1:
                    fruits[1][1] = i
                fruits[1][2] = i
                total += 1
            else:
                if fruits[0][2] > fruits[1][2]:
                    fruits[1][0] = tree[i]
                    fruits[1][1] = i
                    fruits[1][2] = i
                    total = fruits[0][2] - fruits[0][1] + 2
                else:
                    fruits[0][0] = tree[i]
                    fruits[0][1] = i
                    fruits[0][2] = i
                    total = fruits[1][2] - fruits[1][1] + 2
            if total > maxTotal:
                maxTotal = total
        return maxTotal

s = Solution()
tree = [3,3,3,1,2,1,1,2,3,3,4]
print( s.totalFruit(tree) )