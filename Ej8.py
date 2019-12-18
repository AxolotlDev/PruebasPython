#Ejercicio 8
#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
Sb = int(input("Ingrese el sueldo base del vendedor: "))
vent = int(input("Ingrese la cantidad de ventas hechas en el mes: "))
com = (Sb * 0.1 * vent)
tot = (Sb + com)
print(f"Siendo el sueldo base ${Sb} con un extra de 10% extra por venta, con {vent} ventas, son ${com} extra, generando un total de ${tot}")