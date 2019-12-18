#Ejercicio 16
#Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un 
#algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) 
#alcanzará el vehículo más rápido al otro.

dist = float(input("Teniendo en cuenta que el auto 1 va a una velocidad de 50 km/h y el auto 2 a una velocidad de 70 km/h \n Para calcular  en cuantos minutos el auto 2 alcanzara al auto 1 \n Proporcionar una distancia entre ambos autos(Km) : "))
va1 = 50
va2 = 70
tiemp = (dist/(va2 -va1))*60
distf = 70 * tiemp/60
print(f"El auto 2 alcanzara al auto 1 en {tiemp} minutos en una distancia de {distf}Km. tomando como punto 0 la posicion del auto 2.")