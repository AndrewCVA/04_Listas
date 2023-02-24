'''
Escriba un programa Python para multiplicar todos los elementos de una lista
'''

#Entarda

lista = []
multi = 1

#Proceso

for i in range(5):
    n1 = int(input("Ingrese numero entero: "))
    lista.append(n1)
    
    multi = multi * n1

#Salida
    
print(f"la multiplicacion de sus numeros es: {multi}")
print(lista)