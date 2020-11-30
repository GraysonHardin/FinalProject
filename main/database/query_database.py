def select_all_vehicles(conn):
    """Query all rows of vehicle table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM vehicle")

    rows = cur.fetchall()

    return rows  # return the rows
