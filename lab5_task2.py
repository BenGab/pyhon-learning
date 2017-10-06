#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3 as dbapi
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('dbname', nargs=1, type=str, help='Name of the database')
    parser.add_argument('country', nargs=1, type=str, help='Name of the country')
    try:
        return parser.parse_args()
    except Exception as ex:
        parser.print_help(); print(ex)

def get_capital(country, db):
    with dbapi.connect(db) as db:
        cursor = db.cursor()
        try:
            cursor.execute('SELECT City.Name from City, Country WHERE Country.Capital=City.ID AND Country.Name = ?', (country,))
            row = cursor.fetchone()
            if row is None:
                print('Capital was not found.')
                exit(1)
            else:
                print('The capital of %s is %s' % (country, row[0]))
        except Exception as ex:
            print(ex)


def main():
    args = get_args()
    get_capital(args.country[0], args.dbname[0])

if __name__ == '__main__':
    main()