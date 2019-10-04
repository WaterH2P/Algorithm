
import os

N = [ x*x for x in range(1, 11) ]
print(N)

L = [ x*x for x in range(1, 11) if x % 2 == 0 ]
print(L)

S = [ m+n for m in 'ABC' for n in 'abc' ]
print(S)

F = [ d for d in os.listdir('.') ]
print(F)

Ss = ['Hello', 'World', 'My', 'Name', 'Is', 'H2P']
print( [ s.lower() for s in Ss ] )

num = 11
string = 'abc'
print( isinstance(num, int) )
print( isinstance(string, str) )