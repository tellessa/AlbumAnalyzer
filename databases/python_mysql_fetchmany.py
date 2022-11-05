from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def iter_row(cursor, size=10):
    """ generator that chunks db into series of fetchmany() calls"""
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row


def query_with_fetchmany():
    """ Use iter_row() generator to fetch 10 rows at a time """
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM books")

        for row in iter_row(cursor, 10):
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    query_with_fetchmany()
