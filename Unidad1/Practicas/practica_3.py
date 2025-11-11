#Practica 3. Introduccion al polimorfismo 
#Simular un sistema de cobro de al menos 4 tipos
class pago_tarjeta:
    def procesar_pago(self,cantidad):
        return f"Procesando pago de ${cantidad} con tarjeta de debito/credito"

class paypal:
    def __init__(self,__nombre_us):
        self.__nombre_us=__nombre_us #Dato/ Atributo privado
        
    def procesar_pago(self,cantidad):
        if self.__nombre_us==input("Ingresar el nombre de usuario: "):
           return f"Procesando pago de ${cantidad} con paypal"
    
class oxxo:
    def procesar_pago(self,cantidad):
        COMICION=20
        cantidad+=COMICION
        return f"Procesando pago de ${cantidad} con dinero en efectivo en oxxo"

    
class bales_despensa:
    def procesar_pago(self,cantidad):
        return f"Procesando pago de ${cantidad} con dinero en efectivo en oxxo"    
metodos_pago=[pago_tarjeta(),oxxo(),bales_despensa()]

for i in metodos_pago:
    print(i.procesar_pago(500))
    
#Actividad 1
#Procesar diferentes cantidades en cada opcion de pago: 100 con tarjeta, 400 con paypal, 600 con deposito y 5000 con cheque

pago1 = pago_tarjeta()
pago2 = paypal("Jesus")
pago3 = oxxo()
pago4 = bales_despensa()

print("\n"+pago1.procesar_pago(100))
print(pago2.procesar_pago(400))
print(pago3.procesar_pago(600))
print(pago4.procesar_pago(5000))

#Actividad 2.agragar funcionalidad adicional a metodo procesar_pago() cuando sea deposito: sumar $20 (comision) a cantidad
#Cuando sea paypal, pedir al usuario su nombre