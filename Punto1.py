#Miguel Troya and Billinwg Paternina

print("programas: \n Ingenieria de sistemas: 2.000.000 \n Ingenieria electronica: 2.300.000 \n Ingenieria mecatrinica: 4.500.000 \n Ingenieria sistemas complejos 3.500.000 ")

Proma = int(input(" DIgite 1: Ingenieria de sistemas 2: Ingenieria electronica 3: Ingenieria mecatronica 4: Ingenieria sistemas complejos: "))

#El costo de la matricula va a tener algunas variaciones según los siguientes criterios:
EstrSoc = int(input(" Digite el estrato socioeconomico al que pertenece: "))
UltimValPen = float(input(" Digite el ultimo valor de pension:  $"))
PatriFam = float(input(" Digite en pesos el valor del patrimonio familiar del estudiante: $"))
edad = int(input("ingrese su edad "))


#Descuentos para realizar en todas las carreras, iniciendo en 0 por si no se cumple
#Si las condiciones se cumplen cambiaran de valor
DescuentoEstrSoc = 0
IncrementoUltimValPen = 0
IncrementoPatriFam = 0
DescuentoEdad = 0


#Ingenieria de sistemas
if Proma == 1:
    ValorIngSistemas = 2000000

    if EstrSoc <=3:
        DescuentoEstrSoc = (ValorIngSistemas*5)/100

    if UltimValPen >= 500000:
        IncrementoUltimValPen = (ValorIngSistemas*15)/100

    if PatriFam > 200000000:
        IncrementoPatriFam = (ValorIngSistemas*1.5)/100

    if edad >= 18:
        DescuentoEdad = 50000
    else: DescuentoEdad = 100000

    print(" Valor de la matricula de Ingenieria de sistemas ")
    print(ValorIngSistemas - DescuentoEdad - DescuentoEstrSoc + IncrementoPatriFam + IncrementoUltimValPen )

#Ingenieria electronica
elif Proma == 2:
    ValorIngElectronica = 2300000

    if EstrSoc <=3:
        DescuentoEstrSoc = (ValorIngElectronica*5)/100

    if UltimValPen >= 500000:
        IncrementoUltimValPen = (ValorIngElectronica*15)/100

    if PatriFam > 200000000:
        IncrementoPatriFam = (ValorIngElectronica*1.5)/100

    if edad >= 18:
        DescuentoEdad = 50000
    else: DescuentoEdad = 100000

    print(" Valor de la matricula de Ingenieria electronica ")
    print(ValorIngElectronica - DescuentoEdad - DescuentoEstrSoc + IncrementoPatriFam + IncrementoUltimValPen)

# Ingenieria mecatronica
elif Proma == 3:
    ValorIngMecatronica = 4500000

    if EstrSoc <=3:
        DescuentoEstrSoc = (ValorIngMecatronica*5)/100

    if UltimValPen >= 500000:
        IncrementoUltimValPen = (ValorIngMecatronica*15)/100

    if PatriFam > 200000000:
        IncrementoPatriFam = (ValorIngMecatronica*1.5)/100

    if edad >= 18:
        DescuentoEdad = 50000
    else: DescuentoEdad = 100000

    print(" Valor de la matricula de Ingenieria mecatronica ")
    print(ValorIngMecatronica - DescuentoEdad - DescuentoEstrSoc + IncrementoPatriFam + IncrementoUltimValPen )

#Ingenieria sistemas complejos
elif Proma == 4:
    ValorIngSistemasCoplejos = 4500000

    if EstrSoc <=3:
        DescuentoEstrSoc = (ValorIngSistemasCoplejos*5)/100

    if UltimValPen >= 500000:
        IncrementoUltimValPen = (ValorIngSistemasCoplejos*15)/100

    if PatriFam > 200000000:
        IncrementoPatriFam = (ValorIngSistemasCoplejos*1.5)/100

    if edad >= 18:
        DescuentoEdad = 50000
    else: DescuentoEdad = 100000

    print(" Valor de la matricula de Ingenieria sistemas complejos ")
    print(ValorIngSistemasCoplejos - DescuentoEdad - DescuentoEstrSoc + IncrementoPatriFam + IncrementoUltimValPen)

else: 
    print("El dato ingresado no es valido")





