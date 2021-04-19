"""Algoritmo que permita obtener el promedio de la cantidad de números que el usuario desee digitar, preguntando,
además, si desea continuar o no"""

cont = True
n = 0
sum = 0
while cont: #while cont == True:
    
    val = float(input("Digite un valor: "))

    sum = sum + val #sumador o acumulador
    n = n + 1 #contador

    res = str(input("Desea continuar? si/no: "))
    if res == "no":
        cont = False

pro = sum / n
print("El promedio de los números ingresados es: "+str(pro))

