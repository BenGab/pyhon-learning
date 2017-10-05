#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def f_to_c(F):
    return 5 * (int(F)-32) / 9

def c_to_f(C):
    return ((9 * int(C)) + 160) / 5

def main():
    temperature = input('Temperature C/F:').strip()
    reg = re.match(r'(\-?\d{1,3}\s?)([cf])', temperature, re.IGNORECASE)
    if reg is None:
        print('Invalid temparature: ')
        exit(-1)

    grp = reg.groups()
    res = ''
    if grp[1].upper() == 'F':
        res = str(f_to_c(grp[0].strip())) + ' C'
    else:
        res = str(c_to_f(grp[0].strip())) + ' F'
    print(res)

if __name__ == '__main__':
    main()