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
    # Yes, let's put the --help -h option in.
    # That is the first thing a user would do to check the cli.
    # Also, I think it's a convention to use -- instead of single -
    # for long argument (e.g. -infile -> --infile).
    # Single - is used for single character argument (e.g. -i for --infile).
    # TODO help
    parser.add_argument('req_type', choices=['gen-tmp', 'create', 'read',
                                             'update', 'delete'], help="...")
    # parser.add_argument('-user', nargs='?', help="...")
    # parser.add_argument('-pw', nargs='?', help="...")
    parser.add_argument('-infile', nargs='?', type=argparse.FileType('r'),
                        help="The input file name or path.")
    parser.add_argument('-outfile', nargs='?', type=argparse.FileType('w'),
                        help="The output "
                        "file name or path.")
    parser.add_argument('-tid', nargs='?', help='...')
    parser.add_argument('-query', nargs='*', help='...')

    args = parser.parse_args(args)

    # Isn't it usual to just return the args variable above right now
    # and use the returned args variable in the main() function?
    # Basically, all the if statements in the bottom would be moved
    # to the main() function.

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
        # if not args.user:
        #     raise SyntaxError('-user is required for creating data.')
        # if not args.pw:
        #     raise SyntaxError('-pw is required for creating data.')
        if not args.infile:
            raise SyntaxError('-infile is required for creating data.')
        # handler.create(args.user, args.pw, args.infile)
        handler.create(args.infile)

    if args.req_type == 'read':
        if not args.query:
            raise SyntaxError('-query is required for reading data.')
        handler.read(args.query)

    if args.req_type == 'update':
        # if not args.user:
        #     raise SyntaxError('-user is required for updating data.')
        # if not args.pw:
        #     raise SyntaxError('-pw is required for updating data.')
        if not args.tid:
            raise SyntaxError('-tid is required for updating data.')
        if not args.query:
            raise SyntaxError('-query is required for updating data.')
        # handler.update(args.user, args.pw, args.tid, args.query)
        handler.update(args.tid, args.query)

    if args.req_type == 'delete':
        if not args.tid:
            raise SyntaxError('-tid is required for deleting data.')
        if not args.query:
            raise SyntaxError('-query is required for deleting data.')
        handler.delete(args.tid, args.query)
    return args


def main():
    # For me, variable __file__ points to
    # /home/jyoun/.local/lib/python3.6/site-packages/tip/views/main.py
    # and I cannot find a log file.www
    # First question is, do we always have to dump the log to a file?
    # Maybe we should consider dumping it IF the user prompts to.
    # For example, we can set up an input argument such as --logfile
    # to have the user specify the location of the dump.
    # Otherwise, we can just print log to the console.
    set_logging(__file__ + '.log')
    parse_args(sys.argv[1:])
