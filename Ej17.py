#Ejercicio 17
#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
#El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.

t1 = int(input("Ingrese hora de salida (en formato de 24hs): "))
t2 = int(input("Ingrese minutos de salida (en formato de 24hs): "))
t3 = int(input("Ingrese segundos de salida (en formato de 24hs): "))
tt = int(input("Ingrese la cantidad de  segundos que atarda en trasladarse: "))
t1seg= (t1*3600)
t2seg= (t2*60)
tfinseg= t1seg + t2seg + t3
tfintrasseg = tfinseg + tt
hh = tfintrasseg//3600 
if (hh >= 24):
	dd = hh//24
	hh = hh-24
mm = (tfintrasseg%3600)//60
ss = (tfintrasseg%3600)%60


print(f"Teniendo una salida a las {t1}:{t2}:{t3}Hs , con {tt} segundos de traslado, llegara {dd} dias despues, a las {hh}:{mm}:{ss} ")
