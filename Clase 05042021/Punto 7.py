"""Algoritmo que cuente los números positivos que introduzca el usuario. 
Mostrar el número de valores positivos introducidos. 
El ciclo se detiene cuando el usuario digite un cero (0) o un número negativo"""


it = 0 # cantidad de iteraciones, o número de enteros positivos
while True:
    val = float(input("Digite el valor: "))
    
    if val != 0 and val > 0:
        it = it + 1
    else:
        break
    
print(it)







   
