#!/usr/bin/env python
# import fibo
# fibo.fib()

# from fibo import fib,fib2
from fibo import *
import sys

def main(*n):
    print("__name__",__name__)
    fib(int(n[1]))
    l = fib2(int(n[2]))
    print(l)

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) ==3:
        main(*sys.argv)
    else:
        print('erreur !')
