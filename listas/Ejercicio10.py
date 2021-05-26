n = int(input("Digite el número de elementos de la lista: "))
lista = []

for i in range (0,n):
    val = int(input(f"Digite el valor de la posición {i}: "))
    lista.append(val)
print(lista[:])
#ordenamiento de mayo a menor (descendente)
for i in range(0,n-1):
    for j in range(i+1, n): 
        if lista[j] > lista[i]: #if lista[j] < lista[i]:
            temp = lista[i]
            lista[i] = lista[j]
            lista[j] = temp
print(lista[:])

'''
#Función sorted
#print(sorted(lista)) #Ordena de manera predeterminada la lista de forma ascendente. No modifica la lista original
#print(lista[:])
#print(sorted(lista, reverse = True)) #Ordena de manera descendente usando el reverse=True. No modifica la lista original
#print(lista[:])

#Método sort
#lista.sort() #ordena de manera ascendente y la lista original se ve modificada
lista.sort(reverse=True) #ordena de manera descendente usando el reverse=True y la lista orignal se ve modificada
print(lista[:])

#https://j2logo.com/python/ordenar-una-lista-en-python/#:~:text=La%20forma%20m%C3%A1s%20sencilla%20de,()%20de%20la%20clase%20list%20.
'''