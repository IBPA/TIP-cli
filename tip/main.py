# -*- coding: utf-8 -*-
"""tip/main.py description

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
from tip.db import crud
from tip.utils import set_logging


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
        help="The path to your input file.")
    parser.add_argument(
        '--outfile', '-O',
        nargs='?',
        type=argparse.FileType('w'),
        help="The path to your output file.")
    parser.add_argument(
        '--tid', '-T',
        nargs='?',
        help='The TIP ID (TID) associated with your query.')
    parser.add_argument(
        '--query', '-Q',
        nargs='*',
        help='The query for your request.')
    parser.add_argument(
        '--logfile', '-L',
        nargs='?',
        type=argparse.FileType('w'),
        help='The path to your log file.')

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
    args = parse_args(sys.argv[1:])
    hc, ha = crud.read_headers()
    if not args.logfile:
        set_logging()
    else:
        set_logging(args.logfile.name)
    if args.req_type == 'gen-tmp':
        if not args.outfile:
            outfile_name = 'output.csv'
        else:
            outfile_name = args.outfile.name
        logging.info(
            'Generating data template file {}'.format(outfile_name))
        with open(outfile_name, 'w') as f:
            csv.writer(f).writerow(hc + ha)
    elif args.req_type == 'create':
        if not args.infile:
            raise SyntaxError('-infile is required for creating data.')
        crud.create(args.infile, hc, ha)
    elif args.req_type == 'read':
        if not args.query:
            raise SyntaxError('-query is required for reading data.')
        crud.read(args.query[0])
    elif args.req_type == 'update':
        if not args.tid:
            raise SyntaxError('-tid is required for updating data.')
        if not args.query:
            raise SyntaxError('-query is required for updating data.')
        crud.update(args.tid, args.query[0])
    elif args.req_type == 'delete':
        if not args.tid:
            raise SyntaxError('-tid is required for deleting data.')
        if not args.query:
            raise SyntaxError('-query is required for deleting data.')
        crud.delete(args.tid, args.query[0])
