# 1349. 参加考试的最大学生数
# 给你一个 m * n 的矩阵 seats 表示教室中的座位分布。如果座位是坏的（不可用），就用 '#' 表示；否则，用 '.' 表示。
# 学生可以看到左侧、右侧、左上、右上这四个方向上紧邻他的学生的答卷，但是看不到直接坐在他前面或者后面的学生的答卷。请你计算并返回该考场可以容纳的一起参加考试且无法作弊的最大学生人数。
# 学生必须坐在状况良好的座位上。


class Solution:
    def maxStudents(self, seats) -> int:
        if len(seats) == 0: return 0

        mem, col = {}, len(seats[0])
        # 座位转换，用 0、1 表示
        seats = [list(map(lambda x: 1 if x == '.' else 0, seat)) for seat in seats]

        def f(seats):
            # 压缩存储，将 0、1 序列看作二进制，转化为 int
            A = int(''.join([''.join(list(map(str, seat))) for seat in seats]), 2)
            if A in mem: return mem[A]

            while len(seats) > 0 and sum(seats[0]) == 0: seats.pop(0)
            if len(seats) == 0: return 0

            maxSeat, seated = 0, 0
            for j in range(col):
                if seats[0][j] == 1:
                    # 不坐人
                    seatsT = [[*seat] for seat in seats]
                    seatsT[0][j] = 0
                    seated = f(seatsT)
                    if seated > maxSeat: maxSeat = seated

                    # 坐人
                    seatsT = [[*seat] for seat in seats]
                    seatsT[0][j] = 0
                    if j > 0:
                        seatsT[0][j-1] = 0                          # 左边
                        if len(seats) > 1: seatsT[1][j-1] = 0       # 左后方
                    if j < col - 1:
                        seatsT[0][j+1] = 0                          # 右边
                        if len(seats) > 1: seatsT[1][j+1] = 0       # 右后方
                    seated = 1 + f(seatsT)
                    if seated > maxSeat: maxSeat = seated

            mem[A] = maxSeat
            return maxSeat
        
        return f(seats)


if __name__ == '__main__':
    s = Solution()
    
    result = 4
    seats = [['#','.','#','#','.','#'], ['.','#','#','#','#','.'], ['#','.','#','#','.','#']]
    print(s.maxStudents(seats))

    result = 3
    seats = [['.','#'], ['#','#'], ['#','.'], ['#','#'], ['.','#']]
    print(s.maxStudents(seats))

    result = 10
    seats = [['#','.','.','.','#'], ['.','#','.','#','.'], ['.','.','#','.','.'], ['.','#','.','#','.'], ['#','.','.','.','#']]
    print(s.maxStudents(seats))

    result = 8
    seats = [['#','#','.','#','.'], 
            ['.','.','.','#','.'],
            ['#','#','.','#','#'],
            ['#','#','#','#','#'],
            ['#','.','.','#','.']]
    print(s.maxStudents(seats))
