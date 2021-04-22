#===========================================================================================#
# Miguel Angel Troya Torres
#===========================================================================================#



import math
suma = 0

while True:
    print("\n    CALCULADORA TRIGONOMETRICA "+"\n")

    print("DIGITE")
    funciones = int(input(" 1 para calcular el seno: \n 2 para calcular el coseno: \n 3 para calcular la tangente: \n 4 para calcular el cosecante: \n 5 para calcular la secante: \n 6 para calcular el cotangente: \n 7 para calcular el exponencial: \n 8 para calcular el logaritmo natural: \n 9 para calcular el logaritmo decimal:\n \n"))
    
    if funciones == 1:#El usuario calculara usando la funcion seno
        angulo = int(input(" Digite 1 si es en Grados: \n Digite 2 si es en Radianes: \n"))

        if angulo == 1:
            grado = float(input("Digite numero en grados: "))
            valor = math.radians(grado)
        elif angulo == 2:
            valor = float(input("Digite numero en radianes: "))
        else:
            print("Digitaste una opcion invalida \n")

        for n in range(10):

            fact = 1 
            factorial = (2*n+1)

            for x in range (1,factorial+1):
                fact = fact * x

            termino = (-1)**n * valor ** (2*n+1) / fact
            suma += termino
          

        metpython = math.sin(valor)
        grados1 = math.degrees(valor)
        print(f"El seno de {grados1: .0f}  grados es: {suma: .3f} según serie de McLaurin, y según los métodos de Python es: {metpython: .3f}")

    elif funciones == 2: #El usuario calculara usando la funcion coseno

        angulo = int(input(" Digite 1 si es en Grados: \n Digite 2 si es en Radianes: \n"))

        if angulo == 1:
            grado = int(input("Digite numero en grados: "))
            valor = math.radians(grado)
        elif angulo == 2:
            valor = float(input("Digite numero en radianes: "))
        else:
            print("Digitaste una opcion invalida \n")
        suma=0
        for n in range(10): 
            fact = 1
            factorial = (2*n) 

            for x in range(1,factorial+1):
                fact = fact * x

            termino = (-1)**n * valor ** (2*n) / fact
            suma += termino                  
            

        metpython = math.cos(valor)
        grados1 = math.degrees(valor)
        print(f"El coseno de {grados1: .0f}  grados es: {suma: .3f} según serie de McLaurin, y según los métodos de Python es: {metpython: .3f}")

    elif funciones == 3:#El usuario calculara usando la funcion tangente
        angulo = int(input(" Digite 1 si es en Grados: \n Digite 2 si es en Radianes: \n"))

        if angulo == 1:
            grado = int(input("Digite numero en grados: "))
            valor = math.radians(grado)
        elif angulo == 2:
            valor = float(input("Digite numero en radianes: "))
        else:
            print("Digitaste una opcion invalida \n")
        suma=0
        for n in range(10):
            fact = 1 
            factorial = (2*n+1)

            for x in range (1,factorial+1):
                fact = fact * x
            termino = (-1)**n * valor ** (2*n+1) / fact
            suma += termino
        seno = suma

        suma = 0
        for n in range(10): 
            fact = 1
            factorial = (2*n) 

            for x in range(1,factorial+1):
                fact = fact * x

            termino = (-1)**n * valor ** (2*n) / fact
            suma += termino
        coseno = suma     
                     
        tangente = seno / coseno               

        metpython = math.sin(valor)/math.cos(valor)
        grados1 = math.degrees(valor) 
        print(f"La tangente de {grados1: .0f}  grados es: {tangente: .3f} según serie de McLaurin, y según los métodos de Python es: {metpython: .3f}")

    elif funciones == 4: #El usuario calculara usando la funcion cosecante
        angulo = int(input(" Digite 1 si es en Grados: \n Digite 2 si es en Radianes: \n"))

        if angulo == 1:
            grado = float(input("Digite numero en grados: "))
            valor = math.radians(grado)
        elif angulo == 2:
            valor = float(input("Digite numero en radianes: "))
        else:
            print("Digitaste una opcion invalida \n")
        suma = 0
        for n in range(10):

            fact = 1 
            factorial = (2*n+1)

            for x in range (1,factorial+1):
                fact = fact * x

            termino = (-1)**n * valor ** (2*n+1) / fact
            suma += termino
        cosecante = 1/suma

        metpython = 1/math.sin(valor)
        grados1 = math.degrees(valor)
        print(f"La cosecante de {grados1: .0f}  grados es: {cosecante: .3f} según serie de McLaurin, y según los métodos de Python es: {metpython: .3f}")

    elif funciones == 5: #El usuario calculara usando la funcion secante
        angulo = int(input(" Digite 1 si es en Grados: \n Digite 2 si es en Radianes: \n"))

        if angulo == 1:
            grado = int(input("Digite numero en grados: "))
            valor = math.radians(grado)
        elif angulo == 2:
            valor = float(input("Digite numero en radianes: "))
        else:
            print("Digitaste una opcion invalida \n")
        suma = 0
        for n in range(10): 
            fact = 1
            factorial = (2*n) 

            for x in range(1,factorial+1):
                fact = fact * x

            termino = (-1)**n * valor ** (2*n) / fact
            suma += termino
        secante = 1/suma

        metpython = 1/math.cos(valor)
        grados1 = math.degrees(valor)
        print(f"La secante de {grados1: .0f}  grados es: {secante: .3f} según serie de McLaurin, y según los métodos de Python es: {metpython: .3f}")

    elif funciones == 6:#El usuario calculara usando la funcion cotangente
        angulo = int(input(" Digite 1 si es en Grados: \n Digite 2 si es en Radianes: \n"))

        if angulo == 1:
            grado = int(input("Digite numero en grados: "))
            valor = math.radians(grado)
        elif angulo == 2:
            valor = float(input("Digite numero en radianes: "))
        else:
            print("Digitaste una opcion invalida \n")
        
        for n in range(10): 
            fact = 1
            factorial = (2*n) 

            for x in range(1,factorial+1):
                fact = fact * x

            termino = (-1)**n * valor ** (2*n) / fact
            suma += termino
        coseno = suma 

        suma = 0
        for n in range(10):
            fact = 1 
            factorial = (2*n+1)

            for x in range (1,factorial+1):
                fact = fact * x
            termino = (-1)**n * valor ** (2*n+1) / fact
            suma += termino
        seno = suma

        cotangente = coseno/seno

        metpython = math.cos(valor)/math.sin(valor)
        grados1 = math.degrees(valor) 
        print(f"La cotangente de {grados1: .0f}  grados es: {cotangente: .3f} según serie de McLaurin, y según los métodos de Python es: {metpython: .3f}")

    elif funciones == 7: #El usuario calculara usando la funcion exponencial 

        digito = int(input("\nDigite el valor al que desee sacarle la exponencial: "))
        suma=0
        for n in range(10):
            fact = 1
            factorial = (n)
            for x in range(1,factorial+1):
                fact = fact * x
            termino = digito ** n / fact
            suma += termino

        metpython = math.exp(digito)
        print(f"La exponencial de {digito} es : {suma: .3f}")

    elif funciones == 8:#El usuario calculara usando la funcion logaritmo natural 

        digito = float(input("\nDigite el valor al que desea sacarle el logaritmo natural: "))
        
        for n in range(10):
            logNa = ((digito-1)/(digito+1))** (2*n+1)
            termino = (1/(2*n+1) * logNa) * 2
            
            suma = suma + termino

        metpython = math.log(digito)
        print(f"El logaritmo natural de {digito: .0f} es: {suma: .3f}")

    elif funciones == 9:#El usuario calculara usando la funcion logaritmo decimal
        digito = float(input("\nDigite el valor al que desea sacarle el logaritmo decimal: "))
        suma=0
        for n in range (10):
            logDeci = ((digito-1)/(digito+1))** (2*n+1)
            termino = ((1/(2*n+1) * logDeci) * 2)/2.30259

            suma = suma + termino
        metpython = math.log10(digito)

        print(f"El logaritmo decimal de {digito: .0f} es: {suma: .3f}")

    else:
        print("Digitastes una opcion invalida :( ")

    res = str(input("\nDesea empezar de nuevo si/no: "))
    print("\n")
    if res == "no":
        break
    




         


            
