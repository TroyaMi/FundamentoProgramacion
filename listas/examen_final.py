#=======================================================================================================
# Billinwg Kay Paternina - Miguel Troya Torres
#=======================================================================================================

import os #para poder limpiar pantalla
while True:
    algLneal = int(input("1 para realiar suma de vectores \n2 para realizar resta de vectores \n3 para multiplicar por un escalar \n4 para multiplicar entre vectores \n5 para sumar matrices \n6 para restar matrices:   "))

    print(" ")

    if algLneal == 1:
        A = []
        B = []
        C = []

        fl = int(input("Digite el numero de elementos que tendra la lista: "))
        for i in range(0,fl):
            valA = int(input(f"Digite los valores de la lista A {i}: "))
            A.insert(i, valA)
        
        for j in range(0,fl):
            valB = int(input(f"Digite los valores de la lista B {j}: "))
            B.insert(j, valB)

        for s in range(0,fl):
            C.insert(s,A[s] + B[s])
            
            

        print(f"Lista A {A[:]}")
        print(f"Lista B {B[:]}")
        print(f"Lista C {C[:]}")
        res = input("Desea continuar? 1 para seguir, 2 para salir: ")
        if res.capitalize() == 2:   #capitalize pone la primera letra en mayúscula
            os.system("cls") #para Linux es system("clear") Limpiar pantalla
            break
        else:
            os.system("cls") #para Linux es system("clear")
        
    elif algLneal == 2:
        A = []
        B = []
        C = []

        fl = int(input("Digite el numero de elementos que tendra la lista: "))
        for i in range(0,fl):
            valA = int(input(f"Digite los valores de la lista A {i}: "))
            A.insert(i, valA)
        
        for j in range(0,fl):
            valB = int(input(f"Digite los valores de la lista B {j}: "))
            B.insert(j, valB)

        for r in range(0,fl):
            C.insert(r,A[r] - B[r])
            
            

        print(f"Lista A {A[:]}")
        print(f"Lista B {B[:]}")
        print(f"Lista C {C[:]}")
        res = input("Desea continuar? 1 para seguir, 2 para salir: ")
        if res.capitalize() == 2:   #capitalize pone la primera letra en mayúscula
            os.system("cls") #para Linux es system("clear") Limpiar pantalla
            break
        else:
            os.system("cls") #para Linux es system("clear")
        
    elif algLneal == 3 :
        A = []
        a = []
        num = int(input("Digite el valor del escalar: "))
        
    
        fl = int(input("Digite el numero de elementos que tendra la fila: "))
        for i in range(0,fl):
            valA = int(input(f"Digite los valores de la lista A {i}: "))
            A.insert(i, valA)
        for m in range(0,fl):
            a.insert(m,num * A[m])
    
        print(f"Lista A {A[:]}")
        print(f"A {a[:]}")
        res = input("Desea continuar? 1 para seguir, 2 para salir: ")
        if res.capitalize() == 2:   #capitalize pone la primera letra en mayúscula
            os.system("cls") #para Linux es system("clear") Limpiar pantalla
            break
        else:
            os.system("cls") #para Linux es system("clear")

    elif algLneal == 4:
        A = []
        B = []
        ab = 0
        C=[]
        fl = int(input("Digite el numero de elementos que tendra la lista: "))

        for i in range(0,fl):
            valA = int(input(f"Digite los valores de la lista A {i}: "))
            A.insert(i, valA)

        for j in range(0,fl):
            valB = int(input(f"Digite los valores de la lista B {j}: "))
            B.insert(j, valB)

        for i in range(0,fl):
            C.insert(i, A[i]*B[i])
        for i in range(0,fl):
            ab += C[i]
            

        print(f"Lista A {A[:]}")
        print(f"Lista B {B[:]}")
        print(f"Total:{ab}")
        res = input("Desea continuar? 1 para seguir, 2 para salir: ")
        if res.capitalize() == 2:   #capitalize pone la primera letra en mayúscula
            os.system("cls") #para Linux es system("clear") Limpiar pantalla
            break
        else:
            os.system("cls") #para Linux es system("clear")

    elif algLneal == 5:
        fl = int(input("Digite el número de filas de la matriz: "))
        cl = int(input("Digite el número de columnas de la matriz: "))

        C = []
        A = []
        B= []
        

        for i in range(0,fl):
            A.append([])
            for j in range(0,cl):
                valA = int(input(f"Digite los valores de la lista A {i},{j}: "))
                A[i].append(valA)
        
        for i in range(0,fl):
            B.append([])
            for j in range(0,cl):
                valB = int(input(f"Digite los valores de la lista B {i},{j}: "))
                B[i].append(valB)

        for i in range(0,fl): 
            C.append([])
            for j in range(0,cl):  
                C[i].append(A[i][j]+B[i][j])
            

        print(f"Matriz {A}")
        print(f"Matriz {B}")
        print(f"Matriz {C}")
        res = input("Desea continuar? 1 para seguir, 2 para salir: ")
        if res.capitalize() == 2:   #capitalize pone la primera letra en mayúscula
            os.system("cls") #para Linux es system("clear") Limpiar pantalla
            break
        else:
            os.system("cls") #para Linux es system("clear")
        
    elif algLneal == 6:
        fl = int(input("Digite el número de filas de la matriz: "))
        cn = int(input("Digite el número de columnas de la matriz: "))

        C = []
        A = []
        B=  []
        
        for i in range(0,fl):
            A.append([])
            for j in range(0,cn):
                valA = int(input(f"Digite los valores de la lista A {i},{j}: "))
                A[i].append(valA)
        
        for i in range(0,fl):
            B.append([])
            for j in range(0,cn):
                valB = int(input(f"Digite los valores de la lista B {i},{j}: "))
                B[i].append(valB)

        for i in range(0,fl): 
            C.append([])
            for j in range(0,cn):  
                C[i].append(A[i][j]-B[i][j])
            
        print(A)
        print(B)
        print(C)

        res = input("Desea continuar? 1 para seguir, 2 para salir: ")
        if res.capitalize() == 2:   #capitalize pone la primera letra en mayúscula
            os.system("cls") #para Linux es system("clear") Limpiar pantalla
            break
        else:
            os.system("cls") #para Linux es system("clear")
    else:
        print("La opción digitada no es válida")
        limpiar()
    

            

    


  


        

    



