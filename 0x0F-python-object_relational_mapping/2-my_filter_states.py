#!/usr/bin/python3
"""
  State by name
"""
import sys
import MySQLdb


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    dtbase = sys.argv[3]
    cityName = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=user, passwd=passwd, db=dtbase)
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name="{}"'.format(cityName))
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
