x = float(input("Dgite el valor de x: "))

suma = 0

for n in range(0,10,1):  #for n in range(10)
    #calcular el factorial de n
    fn = 1
    for i in range(1,n+1,1): #"for i in range(1,n+1)"
        fn = fn * i
    ter = x**n / fn #calcula el siguiente término
    suma = suma + ter #acumula el término

print(f"El valor de la serie es {suma:.2f}")

