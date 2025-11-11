import mysql.connector
from mysql.connector import Error

def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '2373203',
            database = 'poo_project_P2'
        )

        if conexion.is_connected():
            print("Conexión MySQL exitosa")
            return conexion

    except Error as e:
        print(f"Error al conectar de tipo {e}")
        return None
    
