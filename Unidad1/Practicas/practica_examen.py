import os

class libro:
    
    def __init__(self,titulo,autor,fecha_a,codigo_libro):
        self.titulo=titulo
        self.autor=autor
        self.fecha_a=fecha_a
        self.codigo_libro=codigo_libro
        self.e_dispos=True
        
    def mostra_iLibro(self):
        print(f"Codigo del libro: {self.codigo_libro}")
        print(f"Titulo del libro: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de lanzamiento {self.fecha_a}")
        
    def marcar_disponible(self):
        if(self.e_dispos==True):
            print("El libro ya esta marcado como disponible")
        else:
            print("El articulo se marcó como disponible") 
            self.e_dispos=True   
        os.system("pause")
        
class usuario:
    
    def __init__(self,ID_usuario,nombre,correo):
        self.ID_usuario=ID_usuario
        self.nombre=nombre
        self.correo=correo
        
    def mostrar_info(self):
        print(f"ID del usuario: {self.ID_usuario}")
        print(f"Nombre del usuario: {self.nombre}")
        print(f"Correo: {self.correo}")
        
    def solicitar_prestamo(self,prestamo,libro):
        print("Se solicita un prestamo...")
        if prestamo.registrar_prestamo(libro.codigo_libro,self.ID_usuario)==True:
            print("El libro se te a otorgado...")
        else:
            print("No se te ha podido entregar este libro")
            
    
        
        
class estudiante(usuario):
    
    def __init__(self,carrera,semestre):
        self.carrera=carrera
        self.semestre=semestre
    
    def mostrar_info(self):
        print(f"ID del Alumno: {self.ID_usuario}")
        print(f"Nombre del Alumno: {self.nombre}")
        print(f"Correo: {self.correo}")
        print(f"Carrera: {self.carrera}")
        print(f"Semestre: {self.semestre}")
        
class profesor(usuario):
    
    def __init__(self,departamento,t_contrato):
        self.departamento=departamento
        self.t_contrato=t_contrato
    
    def mostrar_info(self):
        print(f"ID del Alumno: {self.ID_usuario}")
        print(f"Nombre del Alumno: {self.nombre}")
        print(f"Correo: {self.correo}")
        print(f"Departamento: {self.departamento}")
        print(f"Tipo de contrato: {self.t_contrato}")   

class prestamo():
    
    def __init__(self,libro,usuario,fecha_ip,fecha_devol):
        self.usuario=usuario
        self.libro=libro
        self.fecha_ip=fecha_ip
        self.fecha_devol=fecha_devol
        
    def registrar_prestamo(self,usuario):
        if(self.libro.e_dispos==True):
            print(f"El usuario con id {usuario.nombre} ha adquirido el libro {self.libro.titulo}") 
        else:
            print("Este libro no esta disponible")   
            
    def devolver_libro(self,usuario_dev):
        if(usuario_dev==self.usuario and self.libro.e_dispos==False):
            print("Se devolvio el libro exitosamente")
        else:
            print("No se pudo devolver el libro...")
            
libro_1=libro("Harry Potter","J.K","10-OCT-2025",1)
bot=usuario(1,"Usuario_bot1","user_bot123@gbot.com")
#alumno_1=estudiante(2,"Usuario_bot1","user_bot123@gbot.com","TI","3-4")
#profesor_1
prestamo_1=prestamo(libro_1,bot,"10-OCT-2026","11-OCT-2026")
bot.mostrar_info()
bot.solicitar_prestamo(prestamo_1,libro_1)

            