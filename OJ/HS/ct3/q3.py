string = '12345'
times = 1
while len(string) < 1000000000000:
    string = string + '$'*times + string[::-1]
    times += 1

