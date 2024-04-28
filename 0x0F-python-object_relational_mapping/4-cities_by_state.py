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

    db = MySQLdb.connect(host="localhost",
                         user=username, passwd=passwd, db=dtbase)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name,\
                states.name FROM cities INNER JOIN states ON\
                cities.state_id = states.id ORDER BY cities.id")
    cities = cur.fetchall()

    for city in cities:
        print(city)

    cur.close()
    db.close()
