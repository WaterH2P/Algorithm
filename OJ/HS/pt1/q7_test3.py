def lis(a):
    # print(' '.join(str(i) for i in a))
    print(a[:4], a[:3:-1])


if __name__ == "__main__":
    arr = list(map(int, "1 2 4 7 11 10 9 15 3 5 8 6".split()))
    lis(arr)

