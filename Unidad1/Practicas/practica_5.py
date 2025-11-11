#practica 5. Sigleton
#Ejemplo de patrón de diseño Sigleton - sistema de registro de logs.

class logger:
    #Atributo de la clase para guardar la unica instancia
    _instancia=None

#Método __new__ controla la creacion del objeto antes de init.
#Se asegura que solo exista una unica instancia de logger
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia=super().__new__(cls)
            cls._instancia.archivo=open("app.log","a")    
        return cls._instancia # Devuelve siempre a la misma instancia
    
    def registro(self,mensaje):
        self.archivo.write(mensaje)
        self.archivo.flush() #Fuerza al archivo para guardarse en el disco
        
registro1 = logger() #Creamos la unica instancia SINGLETON
registro2 = logger() #Devuelve la misma instancia , sin crear una nueva

registro1.registro("Inicio de sesion en la aplicacion \n")
registro2.registro("El usuario se autentico \n")

print(registro1 is registro2) # True o false
#Si me regresa True: Es el mismo objeto en memoria.
