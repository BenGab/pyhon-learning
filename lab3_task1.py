#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


def generate_mail(content):
    names = content.split()
    email = u'.'.join(names[::-1])
    return email.encode('ascii'), content


def processfile(path):
    content = []
    with open(path, 'rt') as file:
        content = [generate_mail(x.strip()) for x in file.readlines()]
    for i in content:
        print("Name: " + str(i[0]) + '@dummy.com')
        print(i[1])


def main():
    arguments = sys.argv[1:]
    if len(arguments) > 3 and len(arguments) < 1:
        print("Usage: give at 1 or 3 file(s) to read")
        exit(-1)

    for file in arguments:
        processfile(file)


if __name__ == "__main__":
    main()
