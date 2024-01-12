#!/usr/bin/python3
""" This Module quary a database """


import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )

    cur = db.cursor()
    st = argv[4]
    cur.execute("SELECT name FROM cities WHERE state_id = ( \
            SELECT id FROM states WHERE name = %s) \
            ORDER BY id", (st,))

    result = cur.fetchall()
    if result:
        for row in result:
            print("{}, ".format(row[0])
                  if row != result[-1]
                  else "{}{}".format(row[0], "\n"), end="")
    else:
        print()

    cur.close()
    db.close()
