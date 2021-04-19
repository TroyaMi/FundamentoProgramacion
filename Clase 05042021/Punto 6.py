#Algoritmo que muestre los primeros cinco números pares positivos
import math
#forma 1

npp = 0 #número de pares positivos hallados
n = 1
while npp < 5:
    if math.remainder(n,2) == 0:
        print(n)
        npp = npp + 1
    n = n + 1

#forma 2
val = 0
it = 1
while it <= 5:
    val = val + 2
    print(val)
    it = it + 1
