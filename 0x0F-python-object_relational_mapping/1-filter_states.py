#!/usr/bin/python3
""" This Module quary a database """


import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")

    result = cur.fetchall()
    for row in result:
        print(row)
