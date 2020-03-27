import sys
if __name__ == "__main__":
    for i in range(int(sys.stdin.readline().strip())):
        n = int(sys.stdin.readline().strip())
        nums = list(map(int, sys.stdin.readline().strip().split()))
        canBePair = False
        count = 0
        for num in nums:
            if num > 1: canBePair = True
            if num > 0: count += 1
        if canBePair: print(count + 1)
        else: print(-1)