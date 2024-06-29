import mysql.connector

database = mysql.connector.connect(
    host="db",
    user="backend",
    password="backend.MARIADB.22",
    database="backend",
)
