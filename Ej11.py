#Ejercicio 11
#Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

n1 = float(input("Ingrese el numero 1 : "))
n2 = float(input("Ingrese el numero 2 : "))
dist = abs(n1-n2)
print(f"La distancia ente {n1} y {n2} es: {dist}")