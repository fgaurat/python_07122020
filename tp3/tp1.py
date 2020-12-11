import os
from pathlib import Path
import glob
from pprint import pprint
import argparse
import re

# . \w \b \d 
# ? : 0 ou 1, 
# + : 1 ou n  
# * : 0 ou n
# {1} 1
# {2,} 2 ou n 
# {2,5} 2 ou 5 


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('directory',nargs='?')
    args = parser.parse_args()
    
    p = Path(os.getcwd())
    print(p.parts[-1])
    py_files = glob.glob(f'{args.directory}/*.py')

    for p in py_files:
        l = p.split('/')
        print(l[-1])

    l1 = [p.split('/')[-1] for p in py_files]
    l2 = [Path(p).parts[-1] for p in py_files]

    with open('apache.log','r') as log:
        l = log.readlines()
        for line in l:
            # r = re.findall(r'^\d+\.\d+\.\d+\.\d+', line)
            ip = re.findall(r'^.{7,15}\b', line)

            reg = r'\d{4}:(\d{2}:\d{2}:\d{2}).*HTTP/\d\.\d"\s(\d{3})'
            r = re.findall(reg, line)
            print(r)
            # http_status = re.findall(r'HTTP/\d\.\d"\s(\d{3})', line)
            # if http_status[0] == '404':
            #     print("err",http_status[0])
            #     time_log = re.findall(r'\d{4}:(\d{2}:\d{2}:\d{2})', line)
            #     print(time_log[0])


    html = "<html><h1>le titre</h1></html>"
    r = re.findall(r'<.*?>', html)
    print(r)

if __name__ == "__main__":
    main()

