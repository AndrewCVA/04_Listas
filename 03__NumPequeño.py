'''
Escriba un programa Python para obtener el número más pequeño de una lista
'''

#Entrada

lista = []

#Proceso

for i in range(5):
    valor = int(input("Ingrese valor: "))
    lista.append(valor)
    
men = lista[0]
for i in range(1,5):
    if lista [i] < men:
        men = lista[i]
        posicion = i

#Salida
        
print("Lista completa")
print(lista)

print("Menor de la lista")
print(men)

print("Posicion del menor en la lista")
print(posicion)