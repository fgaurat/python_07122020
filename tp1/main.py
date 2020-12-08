#!/usr/bin/env python

from sequence.fibo import fib,fib2
import json

def main():
    
    l = fib2(1000)
    
    with open("fibo.txt","w") as f:
        # f.writelines(map(lambda v: f"value = {v}\n",l))
        f.writelines([f"value = {v}\n" for v in l])
        # for value in l:
        #     f.write(f"val = {value}\n")
    
    with open("fibo.txt","r") as f:
        l = f.readlines()
        for v in l:
            print(v.strip())
            print(v, end="")
    
    with open("fibo.json","w") as f:
        # d = {"values":[i.strip() for i in l]}
        d = {"values":l}
        json.dump(d,f)
    
    with open("fibo.json","r") as f:
        d = json.load(f)
        print(d)

if __name__ == "__main__":
    main()