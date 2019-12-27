#Ejercicio 5
#Escribe un programa que pida un nombre de usuario y una contraseña.
#Si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.

Us= str(input("Ingrese un Usuario: "))
Pw= str(input("Ingrese una Contraseña: "))

if Us=="pepe" and Pw=="asdasd":
	print("Has entrado al sistema.")
else:
	print("Error 0102: Usuario o clave incorrecta.")