#!/usr/bin/python3
"""
  State with N starting
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    dtbase = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=passwd, db=dtbase)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE \"N%\" ORDER BY id")
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
