# db.py
import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

def conectar():
    try:
        conexion = mysql.connector.connect(**DB_CONFIG)
        return conexion
    except Error as e:
        print(f"Error de conexión a la base de datos: {e}")
        return None

def desconectar(conexion):
    if conexion and conexion.is_connected():
        conexion.close()
