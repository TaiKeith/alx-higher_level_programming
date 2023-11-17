#!/usr/bin/python3
"""
This script lists all states with a name starting with N from
the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Access the database and retrieves all states starting with uppercase N
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
            passwd=argv[2], database=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' \
            ORDER BY states.id ASC")
    result = cur.fetchall()
    for row in result:
        print(row)
