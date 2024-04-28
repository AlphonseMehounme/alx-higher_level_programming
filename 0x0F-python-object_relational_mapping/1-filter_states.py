#!/usr/bin/python3
"""
  State with N starting
"""
import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    dtbase = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=user,
                         passwd=passwd, db=dtbase, port=3306)
    cur = db.cursor()

    cur.execute('SELECT * FROM states WHERE name LIKE "N%" ORDER BY id ASC')
    states = cur.fetchall()

    for state in states:
        print(state)
