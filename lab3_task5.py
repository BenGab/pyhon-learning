#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

def get_perc(percstr):
    return int(percstr[:-1])

def main():
    p = subprocess.Popen(['df', '-P'], stdout=subprocess.PIPE)

    lines = p.stdout.readlines()
    topl = tuple(lines.pop(0).decode('utf-8').split())
    dfs = [(x[0], x[1], x[2], x[3], x[4], x[5], get_perc(x[4])) for x in (tuple(l.decode('utf-8').split()) for l in lines)]
    dfs.sort(key=lambda x: x[6],reverse=True)
    print('%+25s|%+15s|%+15s|%+15s|%+15s|%+15s' % (topl[0], topl[1], topl[2], topl[3], topl[4], topl[5]))
    for x in dfs:
        print('%+25s|%+15s|%+15s|%+15s|%+15s|%+15s' % (x[0], x[1], x[2], x[3], x[4], x[5]))

if __name__ == '__main__':
    main()