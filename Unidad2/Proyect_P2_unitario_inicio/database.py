import mysql.connector
import os
from mysql.connector import Error 
def crear_conexion():
    try:
        conn = mysql.connector.connect(user='root', password='2373203', host='127.0.0.1', database='poo_project_p2')
        resultado=f"\n\t\t\t\t\t     {'\033[0;92m'}{'\033[4;92m'}✅ Conexion a la base de datos realizada ✅ {'\033[0;0m'}"
    except Error as e:
        print(e)
        print("Algo no se pudo completar para obtener los datos del sistema")
        print("Por favor contactar con un administrador ") 
        os.system("cls")
        os.system("pause")
        resultado=f"\n\t\t\t\t\t     {'\033[4;93m'}{'\033[0;93m'}⚠ Ocurrio algo inprevisto en la conexion a la DB... ⚠ {'\033[0;0m'}"
        conn=None
    return resultado,conn
