#Ejercicio 20
#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas 
#tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).
e2 = int(input("Ingrese la cantidad de monedas de 2€ que posee: "))
e1 = int(input("Ingrese la cantidad de monedas de 1€ que posee: "))
c50 = int(input("Ingrese la cantidad de monedas de 50 centimos de € que posee: "))
c20 = int(input("Ingrese la cantidad de monedas de 20 centimos de € que posee: "))
c10 = int(input("Ingrese la cantidad de monedas de 10 centimos de € que posee: "))
mE= e2*2 + e1
cE= c50 *50 + c20 *20 + c10*10
eT = mE + (cE//100)
cT = cE%100

print(f"Contas con {eT}€ y {cT} centimos.")