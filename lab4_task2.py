#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

import sys


def main():
    num = int(sys.argv[1])
    pattern = r'([a-zA-z]{%d}).*\1{%d}.*\b' % (num - 1, num)
    with open('/usr/share/dict/words', 'rt') as file:
        for i in [x.strip() for x in file.readlines() if re.match(pattern, x, re.IGNORECASE) != None]:
            print(i)
    return

if __name__ == '__main__':
    main()