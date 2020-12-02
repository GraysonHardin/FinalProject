from sqlite3 import Error

from main.database.connect_to_db import create_connection


def create_table(conn, sql_create_table):
    """ Creates table with give sql statement
    :param conn: Connection object
    :param sql_create_table: a SQL CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)


def create_tables(database):
    sql_create_vehicle_table = """ CREATE TABLE IF NOT EXISTS vehicle (
                                        id integer PRIMARY KEY,
                                        make text NOT NULL,
                                        model text NOT NULL,
                                        year text NOT NULL,
                                        mileage text NOT NULL,
                                        price text NOT NULL,
                                        color text NOT NULL

                                    ); """

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_vehicle_table)
    else:
        print("Unable to connect to " + str(database))
