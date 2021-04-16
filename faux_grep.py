import fileinput
import sys
import re
from argparse import ArgumentParser

parser = ArgumentParser(description="Faux grep")

parser.add_argument('-i', dest="ignore_case", action="store_true", help="ignore case")
parser.add_argument('-f', dest="show_name", action='store_true', help="show file name")

parser.add_argument('search_term', help="search term")

parser.add_argument('files', nargs="*", help="files to search")

args = parser.parse_args()

search_re = re.compile(args.search_term, re.I if args.ignore_case else 0)

for raw_line in fileinput.input(args.files):
    if search_re.search(raw_line):
        line = raw_line.rstrip()
        if args.show_name:
            print(fileinput.filename(), end=': ')
        print(line)
