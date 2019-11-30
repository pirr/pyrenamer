#!/usr/bin/python
"""
Files renamer
Rename all files in directory by pattern
usage:
# simple replace
>>> rname for_replace to_replace
# replace with regex
>>> rname for_replace to_replace* -rx
"""

import argparse
from renamer import FileRenamer

parser = argparse.ArgumentParser(description='Files renaming by pattern')
parser.add_argument('pattern', metavar='P', type=str, help='pattern for file selecting')
parser.add_argument('rename_to', metavar='R', type=str, help='string to replacing')
parser.add_argument('-rx', action='store_true', help='use regex')
args = parser.parse_args()

if __name__ == '__main__':
    rename = FileRenamer(replace=args.pattern, to=args.rename_to, with_regex=args.rx)
    rename()