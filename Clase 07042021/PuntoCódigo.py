#Leer un número de código de estudiante compuesto por 8 dígitos. Los 4 primeros indican año de ingreso.
#Los dos siguientes indican el programa al que ingresa. Los dos últimos indican el número de lista
# #por ejemplo: 19931938, ingresó en 1993, estudia el programa con código 19 y su número de lista es 38
#Indicar en qué año ingresó, si estudia Sistemas o no (el código es 19) y el número de lista
import math
cod = int(input("Digite el código del estudiante (8 dígitos): "))

numl = cod%100 
#numl = math.remainder(cod,100)
t1 = cod/100
t2 = math.trunc(t1)
#t2 = cod//100

prog = math.remainder(t2,100)
t3 = t2/100
ain = math.trunc(t3)


if prog == 19:
    msg = "estudia Ingeniería de sistemas"
else:
    msg = "no estudia Ingeniería de sistemas"


print(f"El estudiante con código {cod} ingresó en el año {ain} y su número de lista es {numl} El joven {msg}")


#Otra forma de hallarlo
numlista = cod%100 #queda el número de lista. El valor de cod se mantiene intacto

temp1 = cod//100 #quedan los primeros 6 dígitos

prog = temp1%100 #guarda solo los dos últimos dígitos que equivalen al código del programa que estudia

aing = temp1//100 #guarda los 4 primeros dígitos, es decir, el año de ingreso

if prog == 19:
    msg = "estudia Ingeniería de sistemas"
else:
    msg = "no estudia Ingeniería de sistemas"

print(f"El estudiante con código {cod} {msg}, ingresó en el año {aing} y su número de lista es {numlista}")


