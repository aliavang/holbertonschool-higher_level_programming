#!/usr/bin/python3
"""
Script to list all states with name starting with 'N'
"""
if __name__ = "__main__":
    import MySQLdb
    from sys import argv

    con = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          pw=argv[2], db=argv[3])
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'  ORDERED BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    con.close()
