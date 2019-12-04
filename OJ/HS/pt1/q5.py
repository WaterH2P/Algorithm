for i in range(int(input())):
    *raw, a, b, k = list(map(int, ' '.join([input(), input(), input()]).split()))
    print(sorted(raw[a-1:b])[k-1])
