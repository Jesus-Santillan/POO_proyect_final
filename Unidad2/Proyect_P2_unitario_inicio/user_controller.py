from database import crear_conexion

def ver_usuarios():
    (result,conn_2)=crear_conexion()
    
    if not conn_2:
        return[]
    cursor=conn_2.cursor()
    cursor.execute("SELECT ID,username FROM usuarios")
    result=cursor.fetchall()
    conn_2.close()
    return result

def crear_usuarios(username,password):
    (result,conn_2)=crear_conexion()
    
    if not conn_2:
        return False
    cursor=conn_2.cursor()
    cursor.execute("INSERT INTO usuarios (username,password) VALUES (%s,%s)",(username,password))
    conn_2.commit()
    conn_2.close()
    return True

def actualizar_usuarios(id_usuario,new_n_us,pass_in,new_pass):
        (result,conn_2)=crear_conexion()
        if not conn_2:
            return[]
        cursor=conn_2.cursor()
        cursor.execute("SELECT * FROM usuarios where ID==%s and password==%s",(id_usuario,pass_in))
        if cursor.fetchall()!=[]:
            cursor=conn_2.cursor()
            cursor.execute("UPDATE usuarios set username=%s, password=%s where ID==%s and password==%s",(new_n_us,new_pass,id_usuario,pass_in))   
            conn_2.commit()      
        conn_2.close()
        
            
    