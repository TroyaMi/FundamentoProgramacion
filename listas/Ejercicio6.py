'''
Leer un vector A de n elementos, los cuales son números enteros. Hay muchos elementos repetidos. 
Crear un vector B con los elementos de A sin repetir e imprimir los dos vectores por separado. 
'''

A = []
B = []
x = int(input("Digite el número de elementos que tendrá la lista: "))
for i in range(0,x):
    ele = int(input(f"Digite el valor de la posición {i}: "))
    A.insert(i, ele)

B.append(A[0])
pb = 0
for i in range(1,x):
    flag = False
    for j in range(0,pb+1):
        if A[i] == B[j]:
            flag = True
            break
    if flag == False:
        pb = pb + 1
        B.insert(pb,A[i])

print(B[:])


