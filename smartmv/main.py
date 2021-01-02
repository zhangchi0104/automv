#!/usr/local/bin/python3
from smartmv.helpers import load_rules, process_file
from argparse import ArgumentParser

if __name__ == "__main__":
    rules = load_rules('/Users/alexzhang/Projects/smartmv/config.json')
    ap = ArgumentParser()
    ap.add_argument("files", metavar="path/to/file/or/folder",
                    type=str, nargs='+', help="the name of the files")
    ap.add_argument("--rule", "-r", action="store_true", required=False, help="the specified rul")
    args = ap.parse_args()

    for file in args.files:
        if args.rule:
            process_file(file, rules, ap.rule)

        else:
            process_file(file, rules)
