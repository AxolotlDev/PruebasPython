#Ejercicio 9
#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.

Val = float(input("Ingrese el valor total de la compra :"))
Desc = float(input("Ingrese el porcentaje de descuento: "))
ValF = (Val - Val * (Desc/100))
print(f"El valor total es de ${Val}, con un descuento del {Desc}%, el valor final es: ${ValF}")