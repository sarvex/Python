# Script Name	: check_for_sqlite_files.py
# Author		: Craig Richards
# Created		: 07 June 2013
# Last Modified	: 14 February 2016
# Version		: 1.0.1

# Modifications	: 1.0.1 - Remove unecessary line and variable on Line 21

# Description	: Scans directories to check if there are any sqlite files in there 

from __future__ import print_function

import os


def isSQLite3(filename):
    from os.path import isfile, getsize

    if not isfile(filename):
        return False
    if getsize(filename) < 100:
        return False
    with open(filename, 'rb') as fd:
        header = fd.read(100)
    return header[:16] == 'SQLite format 3\000'


log = open('sqlite_audit.txt', 'w')
for r, d, f in os.walk(r'.'):
    for files in f:
        if isSQLite3(files):
            print(files)
            print(f"[+] '{os.path.join(r, files)}' **** is a SQLITE database file **** ")
            log.write(f"[+] '{files}' **** is a SQLITE database file **** " + '\n')
        else:
            log.write(
                f"[-] '{os.path.join(r, files)}' is NOT a sqlite database file"
                + '\n'
            )
            log.write(f"[-] '{files}' is NOT a sqlite database file" + '\n')
