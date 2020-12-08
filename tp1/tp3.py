#!/usr/bin/env python
from functools import reduce

def fib(n):    # write Fibonacci series up to n
    """
    Print a Fibonacci series up to n.    
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n=10):
    """
    Return a Fibonacci series up to n.    
    """
    r = []
    a, b = 0, 1
    while a < n:
        r.append(a)
        a, b = b, a+b
    
    return r

def to_upper(*values):
    r = []
    for v in values:
        r.append(v.upper())

    return r

def name_to_upper(**values):
    r = values.copy()
    if 'name' in r:
        r['name'] = values['name'].upper()

    return r

    
fib(10)
result = fib2(n=12)
print(result)# [0,1,1,2,3,5,8]

r = to_upper("toto","tutu","tata")
print(r)

l = ["toto","tutu","tata","toto","tutu","tata","toto","tutu","tata"]
# r = to_upper("toto","tutu","tata","toto","tutu","tata","toto","tutu","tata")
r = to_upper(*l)
r = to_upper()
l=[
    ["toto","tutu"],
    ["toto","tutu"],
    ["toto","tutu"]
]
r = to_upper(*l)
r = to_upper(["toto","tutu"],["toto","tutu"],["toto","tutu"])


print(r)

d = {
    "firstname":"toto",
    "name":"tutu",
    "city":"Paris",
    "age":44 
}
# r = name_to_upper(firstname="toto",name="tutu",city="Paris",age=44 )

r = name_to_upper(**d)
print(r)

l = [1,2,3,4,5]
r = list(map(lambda i: i*2,l))
print(r)

r = list(filter(lambda i: i%2 ==0,l))
print(r)

# f = lambda a,b: a+b
# r = reduce(f,l)
r = reduce(lambda a,b: a+b,l)

print(r)