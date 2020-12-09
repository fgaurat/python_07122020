import os
from pathlib import Path
import glob
from pprint import pprint
import argparse

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

    pprint(l)
    # for p in py_files:
    #     path = Path(p)
    #     print(path.parts[-1])
    # Path('').parts[-1]

if __name__ == "__main__":
    main()