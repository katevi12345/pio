Algoritmo mayorDeTres
	Definir num1, num2 , num3 Como Entero
	Escribir " Ingrese el numero 1: "
	Leer num1
	Escribir "Ingrese el numero 2: "
	Leer num2
	Escribir " Imngrese el numero 3: "
	Leer num3
	
	si num1 > num2 y num1 > num3 Entonces
		Escribir " el numero mayor es: " , num1
	SiNo
		
		si  num1 > num2 y num1 > num3
			Escribir " el numero mayor es: " , num2
		SiNo
			si  num1 > num2 y num1 > num3
				Escribir " el numero mayor es: " , num3
				
			FinSi
				
FinSi
FinSi

FinAlgoritmo
