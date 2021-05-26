#miLista = []
miLista = ["Juan", "Pedro", "Juanita", "Miguel"]
print(miLista[:]) #muestra toda la lista
print(miLista[2]) #muestra el elemento de la posición 2. La primera posición es cero
print(miLista[-2]) #muestra el elemento de la posición 2 hacia atrás. La primera posición 1. SUB INDICE O POSICIÓN
print(miLista[0:2]) #muestra una porción de la lista. Intervalo cerrado por iz y abierto por der
print(miLista[:2]) #muestra una porción de la lista. Intervalo cerrado por iz y abierto por der. Asume que empieza en cero
print(miLista[1:2]) #muestra solo el elemento de la posición 1. Abierto por la derecha
print(miLista[2:]) #muestra desde la posición 2 hasta el último

#APPEND
miLista.append("Mateo") #agrega un elemento más a la lista. En este caso el elemento Mateo.
print(miLista[:])
nomNuevo = "Lucas"
miLista.append(nomNuevo) #se puede pasar una variable como parámetro del append
print(miLista[:])

#INSERT(posición, valor o variable)
miLista.insert(2,"Luisa") #tienen dos parámetros de entrada (índice o posición, valor a insertar). Permite insertar un elemento en una posición específica
print(miLista[:])

#EXTEND
miLista.extend(["Elibardo", "Alberto", "Adriana"])  #permite agregar varios elementos a la lista. Las pone al final
print(miLista[:])

lista2 = ["Pablo", "Ernesto", "María Luisa"]
miLista.extend(lista2)  #permite agregar varios elementos desde una lista. Las pone al final
print(miLista[:])

#INDEX
print(miLista.index("Pedro")) #muestra el índice o posición de un elemento específico

x = 10 + miLista.index("Pedro") #Como devuelve un valor numérico, lo puedo usar para operaciones matemáticas
print(x)

miLista = ["Juan", "Pedro", "Juanita", "Juan"]
print(miLista.index("Juan")) #cuando se encuentra un elemento dos o más veces, solo muestra el índice del primero

#valor booleano
print("Pedro" in miLista) #devuelve True o False si lo encuentra en la lista

nombre = "Pedro"
print(nombre in miLista)

#COUNT
print("El número de veces que está Juan en la lista es: ", miLista.count("Juan")) #Count devuelve el número de veces que está un valor específico
nombre = "Juan"
print("El número de veces que está Juan en la lista es: ", miLista.count(nombre))
x = 10 + miLista.count("Ximena")
print(x)

#REMOVE
miLista.remove("Juanita") #permite eliminar el elemento Juanita
print(miLista[:])

#POP
miLista.pop() #Elimina el último elemento de la lista
print(miLista[:])

miLista1 = ["Juan", 10, True, 4.56] #Pueden almacenar diferentes tipos de datos
miLista2 = ["Felipe", 24] #Pueden almacenar diferentes tipos de datos
miLista3 = miLista1 + miLista2 #concatenar dos listas
print(miLista3[:])

#MULTIPLICAR
miListaMul = ["Elem1", 34, "Elem3", True] * 2 #modifica la lista para que se duplique en este caso
print(miListaMul[:])

listaEspx = ["Andy", 10, True]
listaEspx = listaEspx * 2 #duplica la lista completa
print(listaEspx)

listaEsp = ["Andy", 10, True]
listaEsp = listaEsp[1:] * 2 #Quedan por fuera los valores que no estén en el intervalo, por tanto duplica solo los de intervalo
print(listaEsp[:])

#LEN
print(len(miListaMul)) #len dice el número de elementos de una lista

#REVERSE
so = ["Windows", "Linux", "macOS"]
print(so[:])
so.reverse()
print(so[:])