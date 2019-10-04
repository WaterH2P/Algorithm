#!/usr/bin/env python3

import functools

print( int('12345', base=8) )

print( int('10', base=2) )

def add(a, b):
    return a+b

f2 = functools.partial(add, b=2)

print(f2(1))