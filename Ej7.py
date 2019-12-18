#Ejercicio 7
#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
#Por ejemplo: 1000 minutos son 16 horas y 40 minutos.
minutos = int(input("Ingrese la cantidad de minutos: "))	
hs = (minutos//60)
mins = (minutos%60)

print(f"{minutos} minutos son {hs} horas y {mins} minutos.")