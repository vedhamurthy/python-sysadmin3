#!/usr/bin/env ptyhon3.6

import argparse
import sys

parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')
args = parser.parse_args()
#print(args)

try:

    f = open(args.filename)
    limit = args.limit
except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(1)

else:
    with f:
        lines = f.readlines()
        lines.reverse()

        print(lines)


        if limit:
            lines = lines[:limit]

        for line in lines:
            print(line.strip()[::-1])
            #print(line.strip())



