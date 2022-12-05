import argparse
import sys

def read_data(args):
    for line in args.datafile:
        # Write code to read data
        raise RuntimeError("Function not implemented yet")


parser = argparse.ArgumentParser(description="...")
parser.add_argument('datafile', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                    help="Data for the challenge")

if __name__ == '__main__':
    args = parser.parse_args()
    data = read_data(args)