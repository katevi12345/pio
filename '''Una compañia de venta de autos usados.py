'''Una compañia de venta de autos usados, paga a su personal de ventas un salario de 
$1000 mensuales, mas una comisión de $150 por cada auto vendido, más el 5% del valor de
la venta de todos los autos. Cada mes el capturista de la empresa ingresa en la computadora los 
datos pertinentes.
Hacer un programa que calcule e imprima el salario mensual de un vendedor dado'''

salarioBase = 1000 

comisionPorAuto = 150

porcentajeVenta = 0.05

autosVendidos = int(input("digite numero de autos vendidos: "))

valorTotalVentas = float(input("ingrese el total de las ventas: "))

comisionTotal = comisionPorAuto* autosVendidos

porcentajeTotalVentas = valorTotalVentas * porcentajeVenta


salarioMensual = salarioBase + comisionTotal + porcentajeTotalVentas

print(f"el resultado mensual del vendedor estafador es {salarioMensual}")


