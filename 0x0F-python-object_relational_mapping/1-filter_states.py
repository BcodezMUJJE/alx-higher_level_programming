#!/usr/bin/python3
"""
1-filter_states - displays all values whose name starts with an upercase `N`
in the states table of hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    av = sys.argv
    ac = len(av) - 1

    user = av[1]
    passwd = av[2]
    db = av[3]

    host = "localhost"
    port = 3306

    conn = MySQLdb.connect(host=host, port=port,
                           user=user, passwd=passwd, db=db)

    cur = conn.cursor()

    cur.execute(
        """SELECT * FROM states
        WHERE name LIKE _utf8mb4 'N%'
        COLLATE utf8mb4_0900_as_cs
        ORDER BY id ASC""")

    rows = cur.fetchall()

    for row in rows:
        print(row)
