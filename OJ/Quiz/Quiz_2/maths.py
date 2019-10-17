# ab % c = ( a%c * b%c ) % c
n = int(input().strip())
for k in range(n) :
    a, b, c = map(int, input().strip().split())
    print(pow(a, b) % c)