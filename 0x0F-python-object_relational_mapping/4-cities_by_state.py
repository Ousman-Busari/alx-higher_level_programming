#!/usr/bin/python3
"""list all cities in the cities table of hbtn_0e_0_usa databse"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name \
                   FROM cities as c \
                   JOIN states as s \
                   ON c.state_id = s.id \
                   ORDER BY c.id")
    cities = cur.fetchall()
    [print(city) for city in cities]
    cur.close()
    db.close()
