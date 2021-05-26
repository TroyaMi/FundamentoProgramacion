#=========================================================================
#Billi Paternina - Miguel Troya 
#=========================================================================


menu = int(input('''
    Digite 1 para mostrar lista que contenga los elementos múltiplos de 2
    Digite 2 para mostrar lista que contenga los factoriales de los elementos de la lista_A
    Digite 3 para mostar lista que contenga los elementos de la lista_A ubicados en las posiciones impares
    '''))

x = int(input("Digite el número de elementos: "))

A = []
B = []
D = []
for i in range (0,x):
    lista_A = int(input(f"Digite el valor de la posición {i}: "))
    A.append(lista_A)
    #A.insert(1, lista_A)

if menu == 1:
    for i in range (0,x):
        if A[i] % 2 == 0:
            B.append(A[i])
            
            
    print(B[:])


#elif menu == 2:
    #for i in range (0,x):


elif menu == 3:
    for i in range (0,x):
        if A[i] % 2 != 1 :
            D.append(A[i])

    print(D[:])




  
