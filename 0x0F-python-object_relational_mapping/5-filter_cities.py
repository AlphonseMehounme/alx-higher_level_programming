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
    statename = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         user=username, passwd=passwd, db=dtbase)
    cur = db.cursor()
    cur.execute("SELECT * FROM cities WHERE state_id = (SELECT id FROM states\
                WHERE name = %s) ORDER BY id", (statename,))
    cities = cur.fetchall()

    i = 0
    for city in cities:
        if i < len(cities) - 1:
            print("{}, ".format(city[2]), end="")
            i += 1
        else:
            print("{}".format(city[2]), end="")
            i += 1
    print()

    cur.close()
    db.close()
