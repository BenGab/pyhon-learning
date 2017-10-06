#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3 as dbapi
import argparse

def get_db_commands(commandfilepath):
    with open(commandfilepath, 'rt') as file:
        return file.read().split(';')

def run_db_commands(dbname, commands):
    executed = 0
    skipped = 0
    with dbapi.connect(dbname) as db:
        cursor = db.cursor()
        for x in commands:
            try:
                cursor.execute(x)
                executed += 1
            except Exception:
                skipped += 1
        db.commit()
    print('Executed commads: %d\n Skipped command: %d' % (executed, skipped))


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('dbname', nargs='?', type=str, help='Name if the database')
    parser.add_argument('sqlfile', nargs='?', type=str, help='Path of the file to open')
    try:
        return parser.parse_args()
    except Exception as ex:
        parser.print_help(); print(ex)


def main():
    args = get_args()
    commands = get_db_commands(args.sqlfile)
    run_db_commands(args.dbname, commands)


if __name__ == '__main__':
    main()