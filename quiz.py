print( "CALCULADORA BASICA")

print("¿Que operacion deceas hacer?")

oper = int(input("Digite 1: Suma. \n Digite 2: Resta \n Digite 3: Multiplicacion. \n Digite 4: Division. \n Digite 5: Exponeciacion: "))

if oper == 1:
    
    suma1 = int(input("Digite el primer nuemero: "))
    suma2 = int(input("Digite el segundo numero: "))
    totalsum = suma1 + suma2
    print("respuesta ",totalsum)

if oper == 2:
    resta1 = int(input("Digite el primer nuemero: "))
    resta2 = int(input("Digite el primer nuemero: "))
    totalrest = resta1 - resta2 
    print("respuesta ", totalrest)

if oper == 3: 
    multipli1 = int(input("Digite el primer nuemero: "))
    multipli2 = int(input("Digite el primer nuemero: "))
    totalmultipli = multipli1*multipli2
    print("respuesta ", totalmultipli)

if oper == 4:
    divic1 =  int(input("Digite el primer nuemero: "))
    divic2 =  int(input("Digite el primer nuemero: "))
    totaldivic = divic1/divic2
    print("respuesta ", totaldivic)

if oper == 5:
    expo1 =  int(input("Digite el primer nuemero: "))
    expo2 =  int(input("Digite el primer nuemero: "))
    totalexpo = expo1**expo2
    print("respuesta ", totalexpo)

else:
    print("digito invalido")



    

