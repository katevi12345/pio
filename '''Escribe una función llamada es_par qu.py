'''Escribe una función llamada es_par que reciba número
y devuelva el mayor de los dos'''

def es_par(numero):
    return numero%  2 == 0
num = int(input("ingrese un numero"))
validacion = es_par(num)
print(validacion)  