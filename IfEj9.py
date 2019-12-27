#Ejercicio 9
#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);

n1 = float(input("Ingrese un primer numero: "))
n2 = float(input("Ingrese un segundo numero: "))
n3 = float(input("Ingrese un tercer numero: "))
vals = [n1,n2,n3]
vals.sort(reverse=True)
print(f"Los valores ordenados de mayor a menor son : {vals}")
