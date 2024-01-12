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
    arg = "{}".format(argv[4])
    q = "SELECT * FROM states WHERE name LIKE %s ORDER BY id"
    cur.execute(q, (arg,))

    result = cur.fetchall()
    for row in result:
        print(row)

    cur.close()
    db.close()
