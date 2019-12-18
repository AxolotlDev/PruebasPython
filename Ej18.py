#Ejercicio 18
#Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
import re
name = str(input("Ingrese su nombre completo, con ambos apellidos: "))
m = re.findall('([A-Z])[A-Za-z]* *', name)
iniciales = "".join(m)
print(m, iniciales)