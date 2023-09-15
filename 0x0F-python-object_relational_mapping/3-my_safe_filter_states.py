#!/usr/bin/python3
"""
3-my_safe_filter_states - this displays all values whose name matches the passed
argument in the states table of hbtn_0e_0_usa using argument sanitization.
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    av = sys.argv
    ac = len(av) - 1

    user = av[1]
    passwd = av[2]
    db = av[3]
    search = av[4]

    host = "localhost"
    port = 3306

    conn = MySQLdb.connect(host=host, port=port,
                           user=user, passwd=passwd, db=db)

    cur = conn.cursor()

    cur.execute(
        """SELECT * FROM states
        WHERE name = _utf8mb4 %s COLLATE utf8mb4_0900_as_cs
        ORDER BY id ASC""", (search,))

    rows = cur.fetchall()

    for row in rows:
        print(row)
