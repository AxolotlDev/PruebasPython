#Ejercicio 3
#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
import math
CatetoMayor = int(input("Introduzca el valor del cateto mayor: "))
CatetoMenor = int(input("Introduzca el valor del cateto menor: "))
Hipotenusa = (math.sqrt(math.pow(CatetoMenor,2)+math.pow(CatetoMayor,2)))
print(f"Siendo el cateto mayor {CatetoMayor} y el cateto menor {CatetoMenor}, la Hipotenusa del triangulo rectangulo es {Hipotenusa}.")