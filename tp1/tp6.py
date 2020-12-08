#!/usr/bin/env python

# import sequence.fibo

# def main():
#     sequence.fibo.fib(1000)


from sequence import fibo
from sequence.fibo import fib,fib2
def main():
    l = fib2(1000)
    s = f"valeur = {l[0]}"
    print(s)
    s = 'valeur = {} {} {} {} {} {}'.format(l[0],*l)
    print(s)
    d= {"a":2,"b":3}
    s = 'valeur = {a} {b}'.format(**d)
    print(s)

if __name__ == "__main__":
    main()