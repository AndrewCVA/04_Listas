'''
Escriba un programa Python para eliminar duplicados de una lista.
'''

#Entrada

lista = []
total = []

#Proceso

for i in range(10):
    i = int(input("Ingrese valor: "))
    lista.append(i)  
    
    if i not in total:
        total.append(i)

#Salida
    
print("Lista completa")
print(lista)

print("Duplicados eliminados")
print(total)        
    
    