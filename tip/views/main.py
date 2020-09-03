# -*- coding: utf-8 -*-
"""tip/views/main.py description

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
from tip.utils import set_logging
from tip.controllers import handler, get_headers


def parse_args(args):
    """Parse command-line arguments

    Args:
        args (str): sys.argv[1:]

    Returns:
        (dict): Parsed arguments

    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'req_type',
        choices=['gen-tmp', 'create', 'read', 'update', 'delete'],
        help='Select a type of your request.')
    parser.add_argument(
        '--infile', '-I',
        nargs='?',
        type=argparse.FileType('r'),
        help="Provide a path to your input file.")
    parser.add_argument(
        '--outfile', '-O',
        nargs='?',
        type=argparse.FileType('w'),
        help="Provide a path to your output file.")
    parser.add_argument(
        '-tid', '-T',
        nargs='?',
        help='Provide a TIP ID (TID) associated with your query.')
    parser.add_argument(
        '-query', '-Q',
        nargs='*',
        help='Provide a query for your request.')
    # parser.add_argument('-user', nargs='?', help="...")
    # parser.add_argument('-pw', nargs='?', help="...")

    return parser.parse_args(args)


def main():
    """Command-line interface driver. See `tip-cli -h` for more help.

    """
    # For me, variable __file__ points to
    # /home/jyoun/.local/lib/python3.6/site-packages/tip/views/main.py
    # and I cannot find a log file.www
    # First question is, do we always have to dump the log to a file?
    # Maybe we should consider dumping it IF the user prompts to.
    # For example, we can set up an input argument such as --logfile
    # to have the user specify the location of the dump.
    # Otherwise, we can just print log to the console.
    set_logging(__file__ + '.log')
    args = parse_args(sys.argv[1:])
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
    elif args.req_type == 'create':
        # if not args.user:
        #     raise SyntaxError('-user is required for creating data.')
        # if not args.pw:
        #     raise SyntaxError('-pw is required for creating data.')
        if not args.infile:
            raise SyntaxError('-infile is required for creating data.')
        handler.create(args.infile)
    elif args.req_type == 'read':
        if not args.query:
            raise SyntaxError('-query is required for reading data.')
        handler.read(args.query)
    elif args.req_type == 'update':
        # if not args.user:
        #     raise SyntaxError('-user is required for updating data.')
        # if not args.pw:
        #     raise SyntaxError('-pw is required for updating data.')
        if not args.tid:
            raise SyntaxError('-tid is required for updating data.')
        if not args.query:
            raise SyntaxError('-query is required for updating data.')
        handler.update(args.tid, args.query)
    elif args.req_type == 'delete':
        if not args.tid:
            raise SyntaxError('-tid is required for deleting data.')
        if not args.query:
            raise SyntaxError('-query is required for deleting data.')
        handler.delete(args.tid, args.query)
