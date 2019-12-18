#Ejercicio 10
#Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:

#55% del promedio de sus tres calificaciones parciales.

#30% de la calificación del examen final.

#15% de la calificación de un trabajo final.
import statistics as st

n1 = float(input("Ingrese la calificacion parcial numero 1 : "))
n2 = float(input("Ingrese la calificacion parcial numero 2 : "))
n3 = float(input("Ingrese la calificacion parcial numero 3 : "))
exf = float(input("Ingrese la califiacion del examen final: "))
trabajofin = float(input("Ingrese la calificacion del trabajo final: "))
notas = [n1,n2,n3]
promnotas = st.mean(notas)
notafin = (promnotas*0.55 + exf*0.30 + trabajofin * 0.15)

print(f"La nota final es: {notafin}")

