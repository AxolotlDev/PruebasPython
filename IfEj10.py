#Ejercicio 10
#Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos
#circunferencias y las clasifique en uno de estos estados:

#tangentes exteriores
#tangentes interiores

#secantes

#interiores

#exteriores


#concéntricas

import math

x1 = float(input("Ingrese x para la circunferencia 1: "))
y1 = float(input("Ingrese y para la circunferencia 1: "))
r1 = float(input("Ingrese r para la circunferencia 1: "))

x2 = float(input("Ingrese x para la circunferencia 2: "))
y2 = float(input("Ingrese y para la circunferencia 2: "))
r2 = float(input("Ingrese r para la circunferencia 2: "))

distx = abs(x1-x2)
disty = abs(y1-y2)
disC = (math.sqrt(math.pow(disty,2)+math.pow(distx,2)))

if disC > (r1+r2):
	print("Son Circunferencias exteriores.")
elif disC == (r1+r2):
	print("Son Circunferencias tangentes exteriores.")
elif disC <(r1+r2) and disC > (abs(r1-r2)):
	print("Son Circunferencias secantes.")
elif disC == (abs(r1-r2)):
	print("Son Circunferencias tangentes interiores.")
elif disC < (abs(r1-r2)):
	print("Son Circunferencias interiores.")
elif disC == 0:
	print("Son Circunferencias concentricas.")
