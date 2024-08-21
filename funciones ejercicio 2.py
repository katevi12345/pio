def calculadora(operador,x,y):
    def suma(a,b):
        return a + b
    def resta(a,b):
        return a - b 
    def multiplicar(a,b):
        return a * b
    def divicion(a,b):
        if b !=0:
            return a / b
        else: 
            return "error" 
    if operador == "suma":
        return suma(x,y)
    elif operador == "resta":
        return resta(x,y)
    elif operador =="multiplicar":
        return multiplicar(x,y)
    elif operador == "dividir":
        return divicion(x,y)
    else:
        return "operacion no valida"

# ejemplo de uso
resultado = calculadora("suma",9,3)
print(f"resultado:{resultado}")
    
    
        
