import mysql.connector
import os

MYSQL_PASS = os.environ["MYSQL_PASS"]
conn = mysql.connector.connect(host='localhost', database='mysql', user='root', password=MYSQL_PASS)

print()
