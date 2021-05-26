x = int(input("Digite el número de elementos: "))



A = []

B = []

C = []

for i in range(0,x):

    val = int(input(f"Digite el valor de la posición {i} "))

    A.append(val)



for i in range(0,x):

    if A[i] % 2 == 0:

        B.append(A[i])

    if A[i] % 3 == 0:

        C.append(A[i])



print(B[:])

print(C[:])


x = int(input("Digite el número de elementos: "))



A = []

B = []

C = []

for i in range(0,x):

    val = int(input(f"Digite el valor de la posición {i}: "))

    A.append(val)

pb = -1

pc = -1



for i in range(0,x):

    if A[i] % 2 == 0:

        pb = pb + 1

        B.insert(pb, A[i])

    if A[i] % 3 == 0:

        pc = pc +1

        C.insert(pc,A[i])



print(B[:])

print(C[:])