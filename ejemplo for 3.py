n1 = int(input("Digite el primer número que debe ser menor que el segundo: "))

n2 = int(input("Digite el segundo número: "))

f = 1

for i in range(1,n1+1):

    f = f * i

print(f"El factorial de {n1} es {f}")



for i in range(n1+1, n2+1):

    f = f*i

    print(f"El factorial de {i} es {f}")