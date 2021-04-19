#FORMAS DE TRABAJAR EL FOR

#for variable in elemento iterable (range, lista, cadena, etc.):
#    cuerpo del bucle

#La forma más común es trabajar con range: range(start, stop, step)-start no es requerido - stop es requerido
#y no lo incluye - step es el incremento, si no se pone el incremento es de 1

#Forma 1: Range con intervalo. No toma el último valor. Realmente es (valorinicial, valorfinal-1)
for i in range(1,5):
    print(f"Hola Forma 1 valor del iterador: {i}") #lo ejecuta 4 veces y la i toma los valores 1 al 4

#Forma 2: Range con dimensión
for i in range(4): #range(0, 4)
     print(f"Hola Forma 2 valor del iterador: {i}")

#Forma 3: variación de la Forma 1. Se inicializa antes el rango
x = range(1,5) #crear una variable con el rango
for i in x: # se pone el rango
    print(f"Hola Forma 3 valor del iterador: {i}")

#ejemplo 1: mostrar los números del 5 al 10 de 2 en 2
for i in range(5,10,2):
    print(f"Hola ejemplo1 valor del iterador {i}")

#Bucle con LISTAS

lista1 = [23,45,34]
lista2 = ["Juan",35,"Medellín",75.3]

#Forma 4 Este bucle se ejecuta 3 veces porque tiene 3 elementos la lista
for i in [0, 1, 3]:
    print(f"Hola forma 4. Valor del iterador {i}")

#Ejemplo 2 de la forma 4
for i in [3, 4, 5]:
    #p = i**2
    print(f"Hola de Ejemplo 2. Ahora i vale {i} y su cuadrado {i ** 2}")
    #print(f"Hola de Ejemplo 2. Ahora i vale {i} y su cuadrado {p}")

#Esta lista está vacía y por tanto no se ejecuta el ciclo
for i in []:
    print("Hola")


#Forma 5 Bucle definiendo la lista antes y usándola como variable
listaV = [3, 4, 4, 5]
for i in listaV:
    print(f"Hola Forma 5. El iterador vale {i}")

#ejemplo 3. 
for i in ["Juan", "Marcos", 2021]:
    print(f"Hola ejemplo3. Valor del iterador {i}")

#Forma 6 Bucle a partir de una lista y sin necesidad de definir la variable iteradora. Cuando la variable iteradora no se usa
for _ in [0, 1, 2]:
    print("Hola Forma 6")

#Forma 7 Usando una cadena
for i in "UNAC":
    print(f"Dame una {i}")
print("Qué dice?? UNAC!!!")



