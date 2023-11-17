#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and lists all cities
of that state from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Connect to the MySQL server and retrieves all cities from the
    database
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                                 passwd=sys.argv[2], database=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.name, states.name FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s "
                "ORDER BY cities.id ASC", (sys.argv[4],))

    cities = []
    results = cur.fetchall()
    for row in results:
        cities.append(row[0])
    print(", ".join(cities))

    cur.close()
    db.close()
