# -*- coding: utf-8 -*-
"""tip/main.py description

This file contains the driver for the command-line interface (CLI).

Author:
    Fangzhou Li: https://github.com/fangzhouli

"""

import csv
import sys
import logging
import argparse
import textwrap
from tip.db import crud


def parse_args(args):
    """Parse command-line arguments

    Args:
        args (str): sys.argv[1:]

    Returns:
        (dict): Parsed arguments

    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        'req_type',
        choices=['gen-template', 'create', 'read', 'update', 'delete'],
        help="Select a type of your request.")
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
        '--id', '-i',
        nargs='?',
        help="The ID of data associated with your request.")
    parser.add_argument(
        '--values', '-V',
        nargs='*',
        help=textwrap.dedent("""\
        The values of fields of data associated with your request:
        - Each parameter is a pair of a field and a value.
        - A field and a value are separated by exactly a colon.
        - The first parameter must be 'type:compound' or 'type:assay',
            indicating the data type you are updating.
        - Each parameter is separated by exactly a comma.
        - Use quotes for strings containing whitespace(s), (e.g., comments.)
        - Use semicolon/s for strings containing multiple values,
            (e.g., pmid.)"""))
    parser.add_argument(
        '--log-level', '-L',
        choices=[10, 20, 30, 40, 50],
        default=20,
        type=int,
        help=textwrap.dedent("""\
        The specified log level:
        - 50: CRITICAL
        - 40: ERROR
        - 30: WARNING
        - 20: INFO
        - 10: DEBUG"""))
    return parser.parse_args(args)


def main():
    """Command-line interface driver. See `tip-cli -h` for more help.

    """
    args = parse_args(sys.argv[1:])

    logging.basicConfig(
        level=args.log_level,
        format='%(asctime)s %(levelname)s %(filename)s: %(message)s')

    if args.req_type == 'gen-template':
        if not args.outfile:
            outfile_name = 'template.csv'
        else:
            outfile_name = args.outfile.name

        logging.info(
            "Generating data template file {} ...".format(outfile_name))

        hc, ha = crud.read_headers()
        with open(outfile_name, 'w') as f:
            csv.writer(f).writerow(hc + ha)

        logging.info("Generated successfully!")

    elif args.req_type == 'create':
        if not args.infile:
            raise SyntaxError("--infile is required for creating data.")
        hc, ha = crud.read_headers()
        crud.create(args.infile, hc, ha)

    elif args.req_type == 'read':
        if not args.values:
            raise SyntaxError("--values is required for reading data.")
        crud.read(args.values[0])

    elif args.req_type == 'update':
        if not args.id:
            raise SyntaxError("--id is required for updating data.")
        if not args.values:
            raise SyntaxError("--values is required for updating data.")
        crud.update(args.id, args.values[0])

    elif args.req_type == 'delete':
        if not args.id:
            raise SyntaxError("--id is required for deleting data.")
        if not args.values:
            raise SyntaxError("--values is required for deleting data.")
        crud.delete(args.id, args.values[0])
