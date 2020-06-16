import sys
import argparse

def positive_integer(s):
    """return a positive integer is input is convertible"""

    if not s.isdigit() or not int(s) > 0:
        msg = "{} is not a positive integer".format(s)
        raise argparse.ArgumentTypeError(msg)
    else:
        return int(s)

def parse_args(args):

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', nargs = 1, default = 1, type = positive_integer,
        help = "the maximum number of bioassays with a compound")
    args = parser.parse_args(args)

    return args.n[0]

if __name__ == '__main__':

    n = parse_args(sys.argv[1:])
    