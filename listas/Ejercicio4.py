'''
Diseñar un algoritmo que dado un vector de nombres con x elementos, le permita al usuario buscar un nombre completo o 
parte de él dentro de los elementos del vector. El usuario podrá elegir si hace una búsqueda exacta o aproximada. 
En la primera opción solo indicará si el nombre exacto se encuentra en el vector y en qué posición, y para la segunda opción, 
mostrará todos los elementos que contengan el nombre parcial dado por el usuario y la posición asociada dentro del vector
'''
A = []
x = int(input("Digite el número de elementos que tendrá la lista: "))
for i in range(0,x):
    ele = input("Digite el nombre a ingresar: ")
    A.insert(i, ele)

opc = int(input("Digite 1 si va a buscar un texto exacto o 2 si necesita ver todas las coincidencias que contengan la cadena que busca: "))
if opc == 1:
    flag = False
    cadena = input("Digite la cadena exacta a buscar: ")
    for i in range(0,x):
        if A[i] == cadena:
            flag = True
            print(f"Se ha encontrado una coincidencia en la posición {i}")
            break
    if flag == False:
        print("No se encontró el valor buscado en la lista")
elif opc == 2:
    subc = input("Digite la subcadena a buscar: ")
    flag = False
    for i in range(0,x):
        if A[i].find(subc) != -1:
            flag = True
            print(f"Posición donde se ha encontrado coincidencia parcial es {i}, y el nombre fue:{A[i]}")
    if flag == False:
        print("No se encontraron coincidencias parciales")
        


#https://programminghistorian.org/es/lecciones/manipular-cadenas-de-caracteres-en-python
'''
#Concatenar ( + )
msg1 = "Hola"
msg2 = "Mundo 1"
msg3 = msg1 + " "+ msg2
print(msg3)

#Multiplicar
msg1 = "Hola " * 3
msg2 = "Mundo 2"
print(msg1 + msg2)

#Añadir
msg1 = "Hola"
msg1 = msg1 + " Mundo 3" #msg1 += " Mundo 3"
print(msg1)

#MÉTODOS

#Extensión
msg = "Hello World" #Tiene 11 caracteres
print(len(msg))

#Encontrar
msg = "Hola Ingenieros"
print(msg.find("Ingenieros")) #devolverá la posición a partir de la cual encuentra la sub cadena
print(msg.find("Mundo")) #devolverá un -1 para indicar que la subcadena no está en la cadena principal

#Minúsculas - Mayúsculas - Capitalize
msg = "HOLA mundo"
msg2 = msg.lower()
msg3 = msg2.upper()
msg4 = msg.capitalize()
print(msg2)
print(msg3)
print(msg4)

#Reemplazar
msg = "Hello World"
msg2 = msg.replace("o", "ou")  
print(msg2) 

#Cortar
msg = "Hola a todos"
msg2 = msg[2:8] #la posición 8 no la toma. Los intervalos son abiertos por la derecha. Los valores 2 y 8 pueden ser reemplazados por variables
print(msg2)  
'''
