# -*- coding: utf-8 -*-
"""cli/views/main.py description

This file contains the driver for the command-line interface (CLI).

Author:
    Fangzhou Li: https://github.com/fangzhouli

TODO:
    - Example
    - Read
    - help
    - comments

"""

import csv
import sys
import logging
import argparse

from utils import set_logging
from controllers import handler, get_headers


def parse_args(args):
    """Parse command-line arguments

    Args:
        args (str): sys.argv[1:]

    Returns:
        (dict): Parsed arguments

    """
    parser = argparse.ArgumentParser()
    # TODO help
    parser.add_argument('req_type', choices=['gen-tmp', 'create', 'read',
                                             'update', 'delete'], help="...")

    parser.add_argument('-user', nargs='?', help="...")

    parser.add_argument('-pw', nargs='?', help="...")

    parser.add_argument('-infile', nargs='?', type=argparse.FileType('r'),
                        help="The input file name or path.")

    parser.add_argument('-outfile', nargs='?', type=argparse.FileType('w'),
                        default=open('output.csv', 'w'), help="The output "
                        "file name or path.")

    args = parser.parse_args(args)

    if args.req_type == 'gen-tmp':
        logging.info(
            'Generating data template file {}'.format(args.outfile.name))
        hc, ha = get_headers()
        csv.writer(args.outfile).writerow(hc + ha)
        args.outfile.close()

    if args.req_type == 'create':
        if not args.user:
            raise SyntaxError('-user is required for data creation.')
        if not args.pw:
            raise SyntaxError('-pw is required for data creation.')
        if not args.infile:
            raise SyntaxError('-infile is required for data creation.')
        handler.create(args.user, args.pw, args.infile)

    # read

    # update

    # delete

    return args


def main():
    set_logging(__file__ + '.log')
    parse_args(sys.argv[1:])
