#!/usr/bin/python3
"""
Takes argument and displays all values in the states
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306,
            host='localhost')

    cursor = db.cursor()
    cursor.execute('SELECT * from states WHERE name = %s ORDER BY states.id',
                   (sys.argv[4],))
    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
