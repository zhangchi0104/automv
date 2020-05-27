#!/usr/local/bin/python3
from helpers import load_rules, process_file
from argparse import ArgumentParser 


if __name__ == "__main__":
    rules = load_rules('/Users/alexzhang/Projects/smartmv/config.json')
    ap = ArgumentParser()
    ap.add_argument("files", metavar="path/to/file/or/folder", type=str, nargs='+')
    args= ap.parse_args()
    
    for file in args.files:
        process_file(file, rules)



