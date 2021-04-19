#13.Hacer DF y PS que lea un número entero N positivo mayor que 2 y muestre un mensaje que diga 
#si el número leído es primo o no.

import math
import time

n = int(input("Digite un número igual o superior a 2: "))

if n == 2:
    print(f"{n} es el único par primo")
else:
    if math.remainder(n,2) == 0:
        print("El número no es primo porque es par diferente a 2")
    else:
        hallado = False
        i = 3
        while i <= math.trunc((n-1)/2) and hallado == False: 
            if math.remainder(n,i) == 0:
                hallado = True
            #print(i)
            i = i + 2
            


        if hallado == True:
            print(f"El número {n} NO es primo")
        else:
            print(f"El número {n} es primo")



