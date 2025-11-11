import random
# Practica 2. clases, objetos, metodos y atributos

class persona:
    def __init__(self,nombre,apellido,edad):
        #Creacion de atributos
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.__cuenta=None #Atributo privado
        
    def asignar_cuenta(self,cuenta):
        self.__cuenta=cuenta
        print(f"{self.nombre} ahora tienes una cuenta bancaria")
        
    def consultar_saldo(self):
        if self.__cuenta:
            print(f"El saldo de {self.nombre} es de: {self.__cuenta.mostrar_saldo() }") #saldo
        else:
            print(f"{self.nombre} no tiene una cuenta creada")
        
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, mi apellido es {self.apellido}, y tengo {self.edad} años")
        
    def cumplir_a(self):
        self.edad+=1
        print(f"Esta persona cumplió: {self.edad} años")
        
estudian_1=persona("Jesus Emilio","Santillan Fuentes",19)
estudian_2=persona("calitos","Lechuga",16)

estudian_1.presentarse()

estudian_2.presentarse()
estudian_2.cumplir_a()
estudian_2.presentarse()

print(estudian_1.nombre)


#Ejercicio 1.
#Crear una clase , objeto , min 3 atributos y min 3 metodos distintos

class ob_p:
    def __init__(self,t_obP,oculto,nombre,cont):
        #Creacion de atributos
        self.t_obP=t_obP
        self.oculto=oculto
        self.nombre=nombre
        self.cont=cont
    def definir_ObjPast(self):
        ob_p_i=random.randint(0,1)
        match(ob_p_i):
            case 0:
                self.t_obP="Objeto"
            case 1:
                self.t_obP="Pastel"
            case _:
                print("Algo salio mal")        
    def cortar(self,respuesta): 
        if (respuesta==1 and self.t_obP==0):
            objetos="Es un objeto!!!,"
            print(objetos)
            print("Asertaste",end="")
            self.cont+=1
        elif (respuesta==2 and self.t_obP==1):
            pastel="Es un pastel!!!,"
            print(pastel)
            print("Asertaste",end="") 
            self.cont+=1   
        else:
            print(f"No asertaste :(")
              
    def mostrar_puntaje(self):
        print("")   
            
class cuenta_bancaria:
    def __init__(self,num_cuenta,saldo):
        self.num_cuenta=num_cuenta
        self.__saldo=saldo #Dato/ Atributo privado
        
    def mostrar_saldo(self):
        return self.__saldo
    
    def depositar(self,cantidad):
        if cantidad>0:
            self.__saldo+=cantidad
            print(f"se depostio la cantidad de {cantidad} a la cuenta")
        else:
            print("Ingresa una cantidad valida")
            
    def restirar(self,cantR):
        if cantR<=self.__saldo:
            self.__saldo-=cantR
            print(f"se restriro la cantidad de {cantR} de la cuenta")
        else:
            print("Fondos insuficientes")    
        
cuenta1 = cuenta_bancaria("001",500)
estudian_1.asignar_cuenta(cuenta1)
estudian_1.consultar_saldo()

cuenta1.depositar(100)
estudian_1.consultar_saldo()
cuenta1.restirar(20)
estudian_1.consultar_saldo()