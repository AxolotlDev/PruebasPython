#Ejercicio 19
#Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por cada respuesta correcta 5 puntos, 
#por una incorrecta -1 y por respuestas en blanco 0. 
#Imprime el resultado obtenido por el estudiante.
import statistics as st
Pr = int(input("Ingrese la cantidad de preguntas: "))
Rc = int(input("Ingrese la cantidad de respuestas correctas: "))
Ri = int(input("Ingrese la cantidad de respuestas incorrectas: "))
Rnr= Pr - Rc - Ri
Pt = Pr*5
Pct = Rc * 5
Pit = Ri * -1
Calf = Pct - Pit

print(f"Siendo un examen compuesto por {Pr} preguntas, habiendo respondido correctamente {Rc}, incorrectamente {Ri}, y sin responder {Rnr}. \n Suman {Calf}/{Pt} puntos." )