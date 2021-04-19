#2. Hacer algoritmo que muestre los números impares entre 1 y 99 y diga cuántos son.
#Forma 1
import math

c = 0
for i in range(1,100,2):
    print(i)
    c = c + 1
print(f"Se encontraron {c} impares")

#Forma 2
c = 0
for i in range(1, 100):
    x = math.remainder(i,2) 
    if  x != 0: #if math.remainder(i,2) != 0: --- if i%2 != 0:
        print(i)
        
        c = c + 1
print(f"Se encontraron {c} impares")

#3. Hacer algoritmo que muestre los números pares entre 2 y 100 y diga cuántos son.
c = 0
for i in range(2,101,2):
    print(i)
    c = c + 1
print(c)
#Forma 2
c = 0
for i in range(2, 101):
    x = math.remainder(i,2) 
    if  x == 0:
        print(i)
        #print (x)
        c = c + 1
print(c)

#4. Hacer algoritmo que muestre los múltiplos de 13 comprendidos entre los números 1000 y 9999 y decir cuántos son.
c = 0
for i in range(1000, 10000):
    if math.remainder(i,13) == 0:
        c = c + 1
        print(i)
print(c)