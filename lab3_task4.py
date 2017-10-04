#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import argparse
from collections import Counter

def get_hist(num):
    res = ''
    for x in range(int(num)):
        res+='@'
    return res

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--top', type=int ,help='Write top N numbers')
    parser.add_argument('infile', nargs='?', type=str, help='input file path')

    try:
        args = parser.parse_args()
        with open(args.infile, 'rt') as file:
            names = [x.lower() for x in file.readline().split()]
            groupby = Counter(names).items() if args.top is None else Counter(names).most_common(int(args.top))
            for name, cnt in (groupby):
                print('%10s|%+10s|%10d' % (name, get_hist(cnt), cnt))
    except Exception as e:
        parser.print_help(); print(e)


if __name__ == "__main__":
    main()