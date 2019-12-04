C = [0, 0, 1, 1]
for i in range(100):
    if C[-3] != C[-1]:
        C.append(1)
    else:
        C.append(0)
print(C)