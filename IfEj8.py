#Ejercicio 8
#Algoritmo que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el
#mensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad es mayor o igual a
#dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo sea ‘M’, debe
#imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.

n = float(input("Ingrese su nota: "))
e = float(input("Ingrese su edad: "))
s = str(input("Ingrese su sexo indicando con (F) Femenino o (M) Masculino: "))

if n>=5 and e>=18:
	if s=="F" or s=="f":
		print("Aceptada.")
	elif s=="M" or s=="m":
		print("Posible.")
	else:
		print("No acpetada.")
else:
	print("No acpetada.")