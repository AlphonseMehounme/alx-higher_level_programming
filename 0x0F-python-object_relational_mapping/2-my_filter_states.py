#!/usr/bin/python3
"""
  Select States Module
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    dtbase = sys.argv[3]
    cityname = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         user=username, passwd=passwd, db=dtbase)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id".format(cityname))
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
