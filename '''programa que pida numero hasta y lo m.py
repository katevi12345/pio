'''programa que pida numero hasta y lo muestre el programa para cuando se ingrese un numero negativo'''

num = int(input("Ingrese un numero(Ingrese un numero negativo para salir)"))
    
while num >= 0:
    print(f"El numero es: {num}")
    num = int(input("Ingrese otro numero: "))
            