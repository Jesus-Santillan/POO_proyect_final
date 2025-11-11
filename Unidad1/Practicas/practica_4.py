l_tickets=[]
class ticket:
    num_tick=0
    def __init__(self,id,t_ticket,t_prior,desc_tck):
        self.id=id
        self.t_ticket=t_ticket
        self.t_prior=t_prior
        self.estado="pendiente"
        self.desc_tck=desc_tck
        
    def mostrar_ticket(self):
        print("----- Ticket -----")
        print(f"ID: {self.id}")
        match self.t_ticket:
            case 1:
                ttk="software"
            case 2:
                ttk="prueba" 
        print(f"Tipo de tiket: {ttk}") 
        tpr=""
        match self.t_prior:
            case 1:
                tpr="baja"
            case 2:
                tpr="media"  
            case 3:
                tpr="alta"
        print(f"Prioridad: {tpr}")  
        print(f"Estado del ticket: {self.estado}")
        print(f"Descripcion del ticket: {self.desc_tck}")

#Clase padre
class empleado:
    def __init__(self,nombre):
        self.nombre=nombre
        
    def trabajar_ticket(self,ticket):
        print(f"El empleado {self.nombre} revisa el ticket {ticket.id}")

class desarrollador(empleado):
    def trabajar_ticket(self, ticket):
        if ticket.t_ticket=="software":
            print(f"El ticket {ticket.id} fue resulto por {self.nombre}")  
        else:
            print("Este tipo de ticket no se puede resolver por este usuario")
            
class tester(empleado):
    def trabajar_ticket(self, ticket):
        if ticket.t_ticket=="prueba":
                print(f"El ticket {ticket.id} fue resulto por {self.nombre}")  
        else:
            print("Este tipo de ticket no se puede resolver por este usuario")  

class proyect_manager(empleado):
    def asignar_tiket(self,ticket,empleado):
        print(f"{self.nombre} asigno el ticket {ticket.id} al empleado {empleado.nombre} ")
        empleado.trabajar_ticket(ticket)

#Agregar un menu interactivo con while y con if para:
# 1.crear un ticket
# 2.Ver los tickets
# 3.salir del programa

import sys
import os
cb="\033[97m"
os.system("color")
os.system("cls")
dev_1=desarrollador("Carlitos lechuga ")
test_1=tester("Anita la huerfanita")
pr_mg=proyect_manager("El querido lider")
salida=True
while salida==True :
    print(f"{'\033[3;96m'}   \t\t\t\t\t",f"".center(25,'-'),f"{cb} 📑 Gesgtion de tickets 📝 {'\033[96m'}",f"".center(25,'-'),f"\t\t\t   ")
    print(f"\n{cb}")
    print(f"\t\t\t\t\t\t\t  {'\033[93m'}‣ {cb}1)  Crear ticket \n")
    print(f"\t\t\t\t\t\t\t  {'\033[94m'}‣ {cb}2)  Ver ticket {cb}({'\033[36m'}Lista de tickets{cb}) \n")
    print(f"\t\t\t\t\t\t\t  {'\033[34m'}‣ {cb}3)  Asignar ticket \n")
    print(f"\t\t\t\t\t\t\t  {'\033[0;31m'}‣ {cb}4)  Salir \n")
    print(f"{'\033[0;0m'}")
    try:
        opc_materia=int(input(f"\t\t\t\t\t\t\t {'\033[100m'}{'\033[37m'} Ingresa la opción a la que quieras ingresar (numero) ‣ "))
        print(f"{'\033[0;0m'}")
        os.system("cls")
        match opc_materia:
            case 1:
                os.system("cls")
                print(f"   \t\t",f"".center(25,'-'),"⁙",f" Creat ticket ".center(23,' '),"⁙",f"".center(25,'-'),f"\t\t\t   ")
                print(f"{'\033[94m'}1) software ")
                print(f"{'\033[0;31m'}2) prueba {'\033[0;33m'}")
                try:
                    tipo_tk=int(input("Ingresa el numero de la opcion ‣ "))
                    if tipo_tk==1 or tipo_tk==2:
                        match tipo_tk:
                            case 1:
                                tipo_tk=="software"
                            case 2:
                                tipo_tk=="prueba" 
                        os.system("cls")
                        print(f"{'\033[93m'}1) baja ")
                        print(f"{'\033[0;31m'}2) media")
                        print(f"{'\033[0;94m'}3) alta {'\033[0;32m'}")
                        tipo_prior=int(input("Ingresa el numero de la opcion ‣ "))                                    
                        if tipo_prior==1 or tipo_prior==2 or tipo_prior==3:
                            match tipo_prior:
                                case 1:
                                    tipo_prior=="baja"
                                case 2:
                                    tipo_prior=="media"  
                                case 3:
                                    tipo_prior=="alta"      
                            desc_tck=input(f"{'\033[0;36m'}Ingresa la descripcion del ticket ‣ ")
                            l_tickets.append(ticket(ticket.num_tick,tipo_tk,tipo_prior,desc_tck))     
                            os.system("cls")
                            print(f"{'\033[0;0m'}El ticket se guardo...")
                        else:
                            print("Ingresa opciones validas 1 , 2 o 3...") 
                    else:
                        print("Ingresa opciones validas 1 o 2...")    
                except ValueError:
                    print("Ingresa solo numeros enteros que esten en las opciones")
            case 2:
                print(f"   \t\t",f"".center(25,'-'),"⁙",f" Ver tickets ".center(23,' '),"⁙",f"".center(25,'-'),f"\t\t\t   ")
                print("")
                for i in range(0,len(l_tickets)):
                    print(f"{l_tickets[i].id}) Tiket ")
                print("")
                try:
                    num_id=int(input("Ingresa el numero de la opcion ‣ "))
                    for j in range(0,len(l_tickets)):
                        if l_tickets[j].id==num_id:
                            os.system("cls")
                            l_tickets[j].mostrar_ticket()
                    
                except ValueError:
                    print("Ingresa un valor numerico para el numero de ticket")    
            case 3: 
                print(f"   \t\t",f"".center(25,'-'),"⁙",f" Asignar ".center(23,' '),"⁙",f"".center(25,'-'),f"\t\t\t   ")
                print("")      
                try:
                    num_id=int(input("Ingresa el numero de ticket a asignar ‣ "))
                    for j in range(0,len(l_tickets)):
                        if l_tickets[j].id==num_id:
                            os.system("cls")
                            pr_mg.asignar_tiket(l_tickets[j],dev_1) 
                    else:
                        if j==len(l_tickets):
                            print("No se encontraron tickets")  
                except ValueError:
                    print("Ingresa un numero de ticket a buscar...") 
            case 4: 
                print(f"Muchas gracias ;> ....")
                sys.exit()
            case _:
                os.system("cls")
                print(f"‣ Porfavor ingresa opciones validas, opcion tecleada: {opc_materia}. Intentalo otra vez")  
                      
    except ValueError:
        print(f"{'\033[0;0m'}")
        os.system("cls")
        print("‣ Ingresa números para seleccionar una opción. porfavor Intentalo otra vez")
    except KeyboardInterrupt:
        print(f"{'\033[0;0m'}")
        os.system("cls")
        print("No ingreses este tipo de cosas...") 
    os.system("pause")
    os.system("cls")