#===========================================================================================
# Miguel Angel Troya Torres
#===========================================================================================

import math
print("    CALCULADORA TRIGONOMETRICA "+ "\n")


digito = int(input("Digite el numero que desea calcular: "))
radianes = math.radians(digito)

contador = 0

while True:
    funciones = int(input("\n Digite 1 para calcular el seno: \n Digite 2 para calcular el coseno: \n Digite 3 para calcular la tangente: \n Digite 4 para calcular el cosecante: \n Digite 5 para calcular la secante: \n Digite 6 para calcular el cotangente: \n Digite 7 para calcular el exponencial: \n Digite 8 para calcular el logaritmo natural: \n Digite 9 para calcular el logaritmo decimal:\n \n"))
    if funciones == 1:
        for n in range(10):
            contador = contador + (-1)**n * radianes ** (2*n+1) / math.factorial((2*n+1))
            metpython = math.sin(digito)
            print(f"El seno de {digito}  grados es: {contador: .3f} según serie de McLaurin, y según los métodos de Python es: {metpython: .3f}")

    elif funciones == 2:
        for n in range(10):                
            contador = contador + (-1)**n * radianes ** (2*n) / math.factorial((2*n))
            metpython = math.cos(digito)
            print(f"El coseno de {digito}  grados es: {contador: .3f} según serie de McLaurin, y según los métodos de Python es: {metpython: .3f}")

    elif funciones == 3:
        for n in range(10):
            metpython = math.tan(digito)
'''
    elif funciones == 4:
        for n in range(10):
            metpython = math.

    elif funciones == 7:
        for n in range(10):
            contador = contador + digito ** n / math.factorial(n)
            metpython = math.exp(digito)
            print(f"La exponencial de {digito} es : {contador: .3f}")

    elif funciones == 8:
        for n in range(10):
            metpython = math.log(digito)
            print(f"El logaritmo natural de {digito} es: {metpython: .3f}")
'''


            

    
