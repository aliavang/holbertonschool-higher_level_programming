#!/usr/bin/python3
"""
Script to list all states from database
"""
if __name__ = "__main__":
    import MySQLdb
    import sys

    con = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                          pw=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = con.cursor()
    cur.execute("SELECT * FROM states ORDERED BY id ASC")
    for row in cur.fetchall():
    print(row)
    cur.close()
    con.close()
