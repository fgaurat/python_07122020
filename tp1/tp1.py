#!/usr/bin/env python

the_world_is_flat = False

if the_world_is_flat:
    print("Be careful not to fall off!")
    print("Be careful not to fall off!")
else:
    print("pas True")

# print("the world is "+str(the_world_is_flat))
# print("the world is",the_world_is_flat,"toto","tutu",2+2)

word = 'Python'
print(word[2:])

squares = [1, 4, 9, 16, 25]
sq1 = squares[-3:]
sq2 = squares[:2]

sq = squares[:]
sq4 = squares
sq4[0]=12
print(sq)
print(squares)

letters = ['a', 'b', 'c', 'd', 'e','f', 'g']
letters[2:5] = ['C', 'D', 'E','F']
print(letters)

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a,end=",")
    a, b = b, a+b

