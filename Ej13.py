#Ejercicio 13
#Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica. Python3 no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿Cómo se puede calcular?
import math
n1 = float(input("Ingrese un numero: "))
Rq = math.sqrt(n1)
Rc = n1**(1/3)# Para poder calcular una Riz no cuadrada solo se debe elevar el numero por una fraccion de 1 sobre la raiz deseada.

print(f"{n1} tiene una raiz cuadrada de {Rq} y una raiz cubica de {Rc}") 