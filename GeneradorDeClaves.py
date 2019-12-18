#Generador de claves.
from random import SystemRandom


longitud = int(input("Ingrese la longitud de la clave: "))

Car = int(input("¿Desea que contenga caracteres especiales? responde con 0 o 1 : " ))


if Car == 1:
	valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"

if Car == 0: 
	valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

cryptogen = SystemRandom()
p = ""

while longitud > 0:
    p = p + cryptogen.choice(valores)
    longitud = longitud - 1

print(f"Su nueva clave es {p}")