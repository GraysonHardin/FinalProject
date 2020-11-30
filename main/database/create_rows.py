def create_vehicle(conn, vehicle):
    """Create a new vehicle for table
    :param conn:
    :param vehicle:
    :return: vehicle id
    """
    sql = ''' INSERT INTO vehicle(make,model,year)
              VALUES(?,?,?) '''
    cur = conn.cursor()  # cursor object

    cur.execute(sql, vehicle)
    return cur.lastrowid  # returns the row id of the cursor object, the vehicle id

