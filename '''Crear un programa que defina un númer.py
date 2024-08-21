'''Crear un programa que defina un número 1 al 100. El jugador
debe intentar adivinar el número, y el programa le indicará si esta
Caliente o Frio (Caliente 10 unidades o menos del número)'''

import random

numerosecreto = random.randint(1,100)
print("adivinar el numero del 1 al 100")
intento=int(input("ingrese su intento"))

while intento != numerosecreto:
    if intento > numerosecreto:
        diferencia = intento - numerosecreto
    else: 
        diferencia = numerosecreto - intento
        
    if diferencia <= 10:
        print ("caliente")
    else:
        print ("frio")
        
    if intento < numerosecreto:
        print ("numero secreto mayor")
        
    else: 
        print("numero secreto menor")
    intento=int(input("ingrese su intento"))
    
print("ganaste")

    
    