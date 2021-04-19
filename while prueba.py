##While por conteo 
numero = 1
suma = 0 
while numero <= 10:
    suma = suma + numero
    numero = numero + 1
print("La suma es: ", suma)

# white con uso de sentencia utilitaria y valor booleano
while True: #keyword
    print("Hola!")

    res = str(input("Desea continuar si/no: "))
    if res == "no":
        break

#white controlado por evento y variable booleano
res = True
while res:

    print("Hola! ")

    res = str(input("Desea continuar si/no: "))
    if res == "no":
        res = False

# while controlado por evento
res = "si"
while res == "si":
    print("Hola! ")

    res = str(input("Desea continuar si/no: "))




