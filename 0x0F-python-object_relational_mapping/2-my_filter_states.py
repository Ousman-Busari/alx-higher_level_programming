#!/usr/bin/python3
"""List all states from states table of the database hbtn_0e_0_usa
whose name matches the one supplied by the user as argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name='{}' ORDER BY id"
                .format(sys.argv[4]))
    states = cur.fetchall()
    [print(state) for state in states]
    cur.close()
    db.close()
