"""
max = int(input("Digite el valor máximo de la serie: "))

a,b = 0,1 #equivale a a = 0 , b = 1

ct = 2

print(a)

print(b)



while a+b < vmax:

    #hallar nuevo término, mostrar nuevo término, contar nuevo término, actualizar valor de a y b

    nt = a + b

    print(nt)

    ct = ct + 1

    a = b

    b = nt

print(f"El número de términos inferiores a {vmax} de la serie fibonacci es {ct}")
"""
print("Mostrar los primeros 20 elementos de la serie de fibonacci")

elemen = 20
a,b = 0,1
ct = 2
print(a)
print(b)

for i in range(0,elemen+1):

    nt = a + b 
    print(nt)
    
    ct = ct +1
    a = b
    b = nt