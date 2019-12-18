#Ejercicio 6
#Calcular la media de tres números pedidos por teclado.
import statistics as st

n1 = int(input("Ingrese numero 1: "))
n2 = int(input("Ingrese numero 2: "))
n3 = int(input("Ingrese numero 3: "))
media=[n1,n2,n3]
m= st.mean(media)
print(f"La media de los 3 numeros ingresados es {m}")
