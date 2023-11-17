#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and lists all cities
of that state from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Connect to the MySQL server and retrieves all cities from the
    database
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], database=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.name, states.name FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s "
                "ORDER BY cities.id ASC", (argv[4],))

    city_dict = {}
    result = cur.fetchall()
    for row in result:
        city_name, state_name = row
        if state_name not in city_dict:
            city_dict[state_name] = set()
        city_dict[state_name].add(city_name)

    state_name = argv[4]
    if state_name in city_dict:
        cities = city_dict[state_name]
        print(", ".join(cities))
    else:
        pass

    cur.close()
    db.close()
