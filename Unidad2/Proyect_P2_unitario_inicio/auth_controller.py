#controlador encargado de la logica de autentificacion.
#Nos sirve para separar la logica del login para mantener limpio el codigo, de la interfaz.

from database import crear_conexion

def validar_credenciales(usuario,password):
    (mensaje,conn)=crear_conexion()
    print(mensaje)
    if not conn:
        return False
    
    cursor=conn.cursor()
    sql="SELECT * FROM usuarios WHERE username=%s AND password=%s"
    cursor.execute(sql,(usuario,password))
    result=cursor.fetchone()
    
    conn.close()
    return bool(result)
    