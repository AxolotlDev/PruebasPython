#Ejercicio 6
#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

let=str(input("ingrese una letra: "))
 
if let>='a' and let<='z':
    print( "la letra es miniscula.")
elif let>='A' and let<='Z':
    print("la letra es mayuscula.")
elif let=='ñ':
    print( "la letra es miniscula.")
elif let=='Ñ':
	print("la letra es mayuscula.")
else:
	print("El valor ingresado no es una letra.")

    