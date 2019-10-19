# ( a * b ) % c = ( a%c * b%c) % c

def powDiv(a, b, c) :
    if b == 1 :
        return a%c
    elif b % 2 == 0 :
        left = powDiv(a, b/2, c)
        return left ** 2 % c
    elif b % 2 == 1 :
        left = powDiv(a, (b-1)/2, c)
        return (left ** 2 * a%c) % c
n = int(input().strip())
for i in range(n) :
    a, b, c = map(int, input().strip().split())
    print(powDiv(a, b, c))