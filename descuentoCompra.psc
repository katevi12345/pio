Algoritmo descuentoCompra
	Definir valorCompra , totalCompra , descuento Como Real
	
	Escribir " digite el valorCompra: "
	leer valorCompra
	
	Si valorCompra > 100 Entonces
		descuento = valorCompra * 0.10
		totalCompra = valorCompra - descuento
		Escribir " el valor de su compra con descuento es: ", totalCompra
		
	SiNo
		Escribir " el valor de su compra si descuento es: " , valorCompra
		
	FinSi
	
FinAlgoritmo
