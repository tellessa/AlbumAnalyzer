import mysql.connector
from mysql.connector import Error
import os


print()


def connect():
    """Connect to MYSQL database"""
    conn = None
    try:
        MYSQL_PASS = os.environ["MYSQL_PASS"]
        conn = mysql.connector.connect(host='localhost',
                                       database='python_mysql',
                                       user='root',
                                       password=MYSQL_PASS)
        if conn.is_connected():
            print("Connected to MySQL database")

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == "__main__":
    connect()
