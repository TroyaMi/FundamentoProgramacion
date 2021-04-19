#while por conteo
numero = 1
suma = 0
while numero <= 10:
    suma = suma + numero
    numero = numero + 1
print("La suma es ",suma)


#while con uso de sentencia utilitaria y valor booleano: break *Buscar cómo se usa con Continue
while True: #keyword
    
    print("Hola")

    res = str(input("Desea continuar si/no"))
    if res == "no":
        break


#while controlado por evento y variable booleana
res = True
while res: #while res == True:
    print("Hola")

    res = str(input("Desea continuar si/no"))
    if res == "no":
        res = False

#while controlado por evento
res = "si"
while res == "si":
    print("Hola")

    res = str(input("Desea continuar si/no"))


