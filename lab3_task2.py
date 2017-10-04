#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    with open('/etc/passwd', 'rt') as file:
        for i in [user for user in (x.strip().split(':') for x in file.readlines()) if user[3] < user[4]]:
            print(i[0])


if __name__ == '__main__':
    main()
