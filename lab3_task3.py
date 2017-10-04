#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from collections import Counter

def get_hist(num):
    res = ''
    for x in range(int(num)):
        res+='@'
    return res

def main():
    arguments = sys.argv[1:]

    if len(arguments) < 1:
        exit(-1)

    with open(arguments[0], 'rt') as file:
       for name, cnt in (Counter([x.lower() for x in file.readline().split()]).items()):
           print('%10s|%+10s|%10d' % (name, get_hist(cnt), cnt))


if __name__ == "__main__":
    main()
