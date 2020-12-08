#!/usr/bin/env python

from sequence.fibo import fib,fib2
def main():
    
    l = fib2(1000)
    
    with open("fibo.txt","w") as f:
        for value in l:
            f.write(f"val = {value}\n")
    

if __name__ == "__main__":
    main()