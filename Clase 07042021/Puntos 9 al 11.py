#9.	Hacer algoritmo que lea un número y muestre su factorial
import math
import time
'''
n = int(input("Digite el entero positivo o cero al que le quiere hallar el factorial: "))
f = 1
for i in range(1, n+1): #se pone n+1 porque no lo tiene en cuenta [1, 3)
    f = f * i
print(f)
print(f"Usando la función de math {math.factorial(n)}")

#10.	Hacer algoritmo que lea dos números N1 y N2 donde N2 > N1. 
#Calcular y mostrar el factorial de todos los números comprendidos entre N1 y N2 incluyéndolos.

#Forma 1
n1 = int(input("Digite el primer número que debe ser menor que el segundo: "))
n2 = int(input("Digite el segundo número: "))
for v in range(n1,n2+1):
    f = 1
    for i in range(1,v+1):
        f = f * i
    print(f"El factorial de {v} es {f}")

#Forma 2 MEJORADA
n1 = int(input("Digite el primer número que debe ser menor que el segundo: "))
n2 = int(input("Digite el segundo número: "))
f = 1
for i in range(1,n1+1):
    f = f * i
print(f"El factorial de {n1} es {f}")

for i in range(n1+1, n2+1):
    f = f*i
    print(f"El factorial de {i} es {f}")

time.sleep(6) #No cierra el archivo ejecutado hasta pasar 6 segundos
'''
#11.El número de combinaciones de m elementos, tomados en grupos de n elementos, 
#viene dado por la fórmula C = m!/(n!*(m-n)!. Hacer algoritmo que lea m y n y calcule y muestre C.
#m debe ser mayor que n. Por ejemplo, se tienen 5 sabores de helado (m) y queremos ver cuántos posibles combinaciones 
#de 3 sabores (n) podemos formar. Comparar con math.comb(m,n)

m = int(input("Digite el primer número: "))
n = int(input("Digite el segundo número: "))

fm = 1
for i in range(1, m+1):
    fm = fm * i

fn = 1
for i in range(1,n+1):
    fn = fn * i

mn = m-n
fmn = 1
for i in range(1,mn+1):
    fmn = fmn * i

c = fm/(fn*fmn)
print(f"Las posibles combinaciones son {c}")