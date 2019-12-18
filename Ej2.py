#Ejercicio 2
#Calcular el perímetro y área de un rectángulo dada su base y su altura.

Alt = int(input("¿Cual es la altura del rectangulo? " ))
Base = int(input("¿Cual es la base del rectangulo? " ))
Perimeto = (Base*2 + Alt*2)
Area = (Base*Alt)
print(f"Dado que la base es {Base} y  la altura {Alt}. El perimetro es {Perimeto} y el area {Area}.")
