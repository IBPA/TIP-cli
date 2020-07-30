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
                        help="The output "
                        "file name or path.")
    parser.add_argument('-keywords', nargs='+', help='...')

    args = parser.parse_args(args)

    if args.req_type == 'gen-tmp':
        if not args.outfile:
            outfile_name = 'output.csv'
        else:
            outfile_name = args.outfile.name
        logging.info(
            'Generating data template file {}'.format(outfile_name))
        hc, ha = get_headers()
        with open(outfile_name, 'w') as f:
            csv.writer(f).writerow(hc + ha)

    if args.req_type == 'create':
        if not args.user:
            raise SyntaxError('-user is required for creating data.')
        if not args.pw:
            raise SyntaxError('-pw is required for creating data.')
        if not args.infile:
            raise SyntaxError('-infile is required for creating data.')
        handler.create(args.user, args.pw, args.infile)

    if args.req_type == 'read':
        if not args.keywords:
            raise SyntaxError('-keywords is required for reading data.')
        handler.read(args.keywords)

    # update

    # delete

    return args


def main():
    set_logging(__file__ + '.log')
    parse_args(sys.argv[1:])