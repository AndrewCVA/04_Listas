'''
Escriba un programa Python para encontrar la lista de palabras
que son más largas que n de una lista dada de palabras
'''

#Entrada

lista =[]
total = []

n = int(input("Cuantas palabras quiere ingresar: "))

#Proceso
        
for i in range (n):
    i = input("Ingrese palabra: ")
    total.append(i)

    if len(i) > 7:
        total.append(i)  

#Salida  
        
print("Lista de palabras:")
print(lista)

print()

print("Lista de palabras mas largas:")
print(total)
    
    