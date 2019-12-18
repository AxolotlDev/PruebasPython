#Ejercicio 12
#Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.
import math
x1 = float(input("Ingrese el x1 : "))
x2 = float(input("Ingrese el x2 : "))
y1 = float(input("Ingrese el y1 : "))
y2 = float(input("Ingrese el y2 : "))
distx = abs(x1-y1)
disty = abs(x2-y2)
Hip = (math.sqrt(math.pow(disty,2)+math.pow(distx,2)))
print(f"La distancia ente el conjunto [{x1},{x2}] y [{y1},{y2}] es: {distx} en x ; {disty} en y , con una distancia entre ambos puntos de {Hip}")