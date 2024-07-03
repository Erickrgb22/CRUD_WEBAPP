# Importar libreria msql.connector
import mysql.connector

database = mysql.connector.connect(
    # Cadena de Conexion con la base de datos de docker en caso de usar
    # Una externa reeplazar host con la ip del servidor SQL
    host="db",
    user="backend",
    password="backend.MARIADB.22",
    database="backend",
)
