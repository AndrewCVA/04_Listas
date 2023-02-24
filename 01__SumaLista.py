'''
Escriba un programa Python para sumar todos los elementos de una lista
'''

#Entrada
lista =[]
suma = 0

#Proceso

for i in range(5):
    n1 = int(input("Ingrese primer valor entero: "))
    lista.append(n1)
    
    suma = suma + n1 

#Salida
    
print(f"la suma de sus numeros es: {suma}")
print(lista)