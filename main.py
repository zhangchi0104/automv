from helpers import load_config
from argparse import ArgumentParser 


if __name__ == "__main__":
    d, conf = load_config('./example.json')
    ap = ArgumentParser()
    ap.add_argument("file", metavar="path/to/file/or/folder", type=str)
    args= ap.parse_args()
    conf[d].run(args.file)