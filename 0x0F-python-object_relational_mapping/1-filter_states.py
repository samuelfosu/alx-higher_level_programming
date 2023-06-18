#!/usr/bin/python3
"""
List all states with a name starting with N
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """Connect to MySQL database"""
    db = MySQLdb.connect(
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in cur.fetchall() if state[1][0] == "N"]
