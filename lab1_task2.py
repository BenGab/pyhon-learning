#!/usr/bin/env python

from __future__ import print_function
from unicodedata import category,normalize
import sys

name = unicode(raw_input("Name: ").strip(), 'utf-8')
names = name.lower().split()
email = u".".join(names[::-1])
email += "@dummy.com"

print(email.encode('ascii'))





