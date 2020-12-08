#!/usr/bin/env python

l = ['toto','titi','tutu','tata']
num = ['123','456','789','101112']

l1 =[v.capitalize() for v in l if v != 'tata']
print(l1)

l2 = [(name,tel)  for i,name in enumerate(l) for i1,tel in enumerate(num) if i == i1]
print(l2)

l3 = list(zip(l,num))
grande_liste = [l,num]

l3 = list(zip(*grande_liste))
print(l3)



t = ([0,1,2],[1,2,3])
t[0][0]=10
print( t)

l4 = [1,2,3,3]
# l4 = list(1,2,3)
print(l4)
# s1 = {1,2,3}
s1 = set(l4)
print(s1)

l = ['toto','titi','tutu','tata']
num = ['123','456','789','101112']

# d['toto'] => 123

d={}
for name in l:
    for n in num:
        d[name] = n

print(d)
for i,name in enumerate(l):
    d[l[i]] = num[i]

print(d)

d ={name:tel  for i,name in enumerate(l) for i1,tel in enumerate(num) if i == i1}
print(d)
    
d = dict(zip(l,num))
print(d)

print( d.keys())

for k in d.keys():
    print(k,d[k])


print( d.items())
for k,v in d.items():
    print(k,v)

d = {
    "DURAND":{
        "name":'DURAND',
        "firstname":'Robert',
        "age":44
    },
    "DUPOND":{
        "name":'DUPOND',
        "firstname":'Jacques',
        "age":44
    },
    "MARTIN":{
        "name":'MARTIN',
        "firstname":'Frédéric',
        "age":44
    },
}

print(d['DURAND'])

for k,v in d.items():
    print(k,v['name'])
    for k1,v1 in v.items():
        print("\t",k1,v1)
