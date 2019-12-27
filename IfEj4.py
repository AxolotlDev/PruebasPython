#Ejercicio 4
#Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.
print("El programa dividira el primer numero por el segundo, en caso de que este ultimo no sea 0.")
n1 = float(input("Ingrese el primer numero: "))
n2 = float(input("Ingrese el segundo numero: "))
if n2 == 0:
	print("El segundo numero es igual a cero, no puede dividirse por 0.")
else:
	n3= n1/n2
	print(f"La division de ambos numeros da como resultado {n3}.")