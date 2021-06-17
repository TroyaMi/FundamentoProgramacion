nf = int(input("Digite el número de filas de la matriz: "))
nc = int(input("Digite el número de columnas de la matriz: "))

m = [] #matriz a llenar por el usuario y para crear las listas A y B
listA = [] #vector de la suma por filas
listB = [] #vector de la suma por columnas

#Llenar la matriz
for i in range(0,nf):
    m.append([]) #agrega una lista a cada posición de la matriz m
    for j in range(0,nc):
        val = int(input(f"Digite el valor de la posición {i},{j}: "))
        m[i].append(val)

#Movimiento por filas para crear ListA
for i in range(0,nf):  
    sf = 0
    for j in range(0,nc):
        sf = sf + m[i][j]
    listA.append(sf)

#Movimiento por columnas para crear ListB
for j in range(0,nc):
    sc = 0
    for i in range(0,nf):
        sc = sc + m[i][j]
    listB.append(sc)

print(m)
print(listA)
print(listB)




        
'''
numf = 4
numc = 3
matriz = []
totalA = []

for i in range(numf):
    matriz.append([])
    for j in range(numc):
        val = int(input(f"Digite el valor para la posición {i} {j}: "))
        matriz[i].append(val)

print(matriz)

#crear una lista con los totales de cada fila
for i in range(numf):
    
    s = 0 
    for j in range(numc):
        s = s + matriz[i][j]
        
    totalA.append(s)
        
print(matriz)
print(totalA)

#crear una lista con los totales de cada columna
'''