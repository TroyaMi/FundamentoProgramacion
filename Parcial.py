import math
print("Calculadora de funciones trigonométricas")
reiniciar = True
while reiniciar == 1:
    op = int(input("Digite el número correspondiente a la función trigonometrica que desea calcular: Para calcular seno digite 1, para calcular coseno digite 2, para calcular tangente digite 3, para calcular cosecante digite 4, para calcular secante digite 5, para calcular cotangente digite 6, para calcular exponencial digite 7, para calcular logaritmo natural digite 8, para calcular logaritmo decimal digite 9: "))

    #Calcular seno
    if op == 1:
        op2 = int(input("Digite 1 si el valor está en grados, digite 2 si el valor está en radianes: "))
        
        if op2 == 1:
            vala = float(input("Digite el valor en grados: "))
            angulo = math.radians(vala)
        
        elif op2 == 2:
            angulo = float(input("Digite el valor en radianes: "))

        else:
            print("Asegurese que la opción digitada corresponda a un valor válido")

        suma = 0
        
        for n in range(0,10,1):
            fn = 1
            fn2 = (2*n)+1

            for s in range(1,fn2+1):
                fn = fn * s
            
            res = pow(-1,n) * pow(angulo,2*n+1) / fn
            suma += res

        python = math.sin(angulo)
        valor = math.degrees(angulo)
        print(f"Según la serie de Taylor el seno de {valor:.3f} grados es {suma:.3f},y según las funciones de python es {python:.3f}")

    #Calcular coseno
    if op == 2:
        op2 = int(input("Digite 1 si el valor está en grados, digite 2 si el valor está en radianes: "))
        
        if op2 == 1:
            vala = float(input("Digite el valor en grados: "))
            angulo = math.radians(vala)
        
        elif op2 == 2:
            angulo = float(input("Digite el valor en radianes: "))

        else:
            print("Asegurese que la opción digitada corresponda a un valor válido")

        suma = 0

        for n in range(0,10,1):
            fn = 1
            fn2 = (2*n)

            for c in range(1,fn2+1):
                fn = fn * c
            
            res = pow(-1,n) * pow(angulo,2*n) / fn
            suma += res 
        
        python = math.cos(angulo)
        valor = math.degrees(angulo)
        print(f"Según la serie de Taylor el coseno de {valor:.3f} grados es {suma:.3f},y según las funciones de python es {python:.3f}")

        #Calcular tangente
    elif op == 3:
        op3 = int(input("Digite 1 si el valor está en grados, digite 2 si el valor está en radianes: "))
        if op3 == 1:
            vala = float(input("Digite el valor en grados: "))
            angulo = math.radians(vala)
        elif op3 == 2:
            angulo = float(input("Digite el valor en radianes: "))
        else:
            print("Asegurese que la opción digitada corresponda a un valor válido")
        suma1 = 0
        for n in range(0,10,1):
            fns = 1
            fn1 = (2*n)+1

            for s in range(1,fn1+1):
                fns = fns * s
            
            res = pow(-1,n) * pow(angulo,2*n+1) / fns
            suma1 += res
            
        suma2 = 0

        for n in range(0,10,1):
            fns2 = 1
            fn2 = (2*n)

            for c in range(1,fn2+1):
                fns2 = fns2 * c
            
            res = pow(-1,n) * pow(angulo,2*n) / fns2
            suma2 += res
        tg = suma1/suma2
        tgpython = math.sin(angulo)/math.cos(angulo)
        valor = math.degrees(angulo)
        print(f"Según la serie de Taylor el coseno de {valor:.3f} grados es {tg:.3f},y según las funciones de python es {tgpython:.3f}")

    #Calcular cosecante
    elif op == 4:
        op4 = int(input("Digite 1 si el valor está en grados, digite 2 si el valor está en radianes: "))
        if op4 == 1:
            vala = float(input("Digite el valor en grados: "))
            angulo = math.radians(vala)
        elif op4 == 2:
            angulo = float(input("Digite el valor en radianes: "))
        else:
            print("Asegurese que la opción digitada corresponda a un valor válido")
        suma1 = 0
    
        for n in range(10):
            fn = 1
            fn2 = 2*n+1
            for s in range(1,fn2+1):
                fn = fn * s 
            res = pow(-1,n) * pow(angulo,2*n+1) / fn
            suma1 += res
        cosc = 1/suma1
        python= 1 / math.sin(angulo)
        valor = math.degrees(angulo)
        print(f"Según la serie de Taylor el coseno de {valor:.3f} grados es {cosc:.3f},y según las funciones de python es {python:.3f}")

    #Calcular secante
    elif op == 5:
        op4 = int(input("Digite 1 si el valor está en grados, digite 2 si el valor está en radianes: "))
        if op4 == 1:
            vala = float(input("Digite el valor en grados: "))
            angulo = math.radians(vala)
        elif op4 == 2:
            angulo = float(input("Digite el valor en radianes: "))
        else:
            print("Asegurese que la opción digitada corresponda a un valor válido")
        suma1 = 0
        for n in range(0,10,1):
            fn = 1
            fn2 = (2*n)

            for c in range(1,fn2+1):
                fn = fn * c
            
            res = pow(-1,n) * pow(angulo,2*n) / fn
            suma1 += res 
        sec = 1/suma1
        python = 1/math.cos(angulo)
        valor = math.degrees(angulo)
        print(f"Según la serie de Taylor la secante de {valor:.3f} grados es {sec:.3f},y según las funciones de python es {python:.3f}")

    #Calcular cotangente
    elif op == 6:
        op3 = int(input("Digite 1 si el valor está en grados, digite 2 si el valor está en radianes: "))
        if op3 == 1:
            vala = float(input("Digite el valor en grados: "))
            angulo = math.radians(vala)
        elif op3 == 2:
            angulo = float(input("Digite el valor en radianes: "))
        else:
            print("Asegurese que la opción digitada corresponda a un valor válido")
        suma1 = 0
        for n in range(0,10,1):
            fns = 1
            fn1 = (2*n)+1

            for s in range(1,fn1+1):
                fns = fns * s
            
            res = pow(-1,n) * pow(angulo,2*n+1) / fns
            suma1 += res
            
        suma2 = 0

        for n in range(0,10,1):
            fns2 = 1
            fn2 = (2*n)

            for c in range(1,fn2+1):
                fns2 = fns2 * c
            
            res = pow(-1,n) * pow(angulo,2*n) / fns2
            suma2 += res
        tg = suma1/suma2
        cotg = 1/tg
        python = 1/math.tan(angulo)
        valor = math.degrees(angulo)
        print(f"Según la serie de Taylor la secante de {valor:.3f} grados es {cotg:.3f},y según las funciones de python es {python:.3f}")

    #Calcular exponencial
    elif op == 7:
        valor = float(input("Digite el valor de x: "))
        suma = 0
        for n in range(10):
            fn = 1
            for i in range (1,n+1,1):
                fn = fn*i
            term = pow(valor,n)/fn 
            suma = suma + term
        print(f"La exponencial de {valor} es {suma:.3f}")
        
    #Calcular logaritmo natural
    elif op == 8:
        res = 0
        x = float(input("Digite el valor de x: "))
        for n in range(10):
            p2 = ((x-1)/(x+1))** (2*n+1)
            p1 = (1/(2*n+1) * p2) * 2
            res = res + p1
        print(f"El logaritmo natural de {x:.0f} es {res:.3f}")

    #Calcular logaritmo decimal 
    elif op == 9:
        res = 0
        x = float(input("Digite el valor de x: "))
        for n in range(10):
            p2 = ((x-1)/(x+1))** (2*n+1)
            p1 = ((1/(2*n+1) * p2) * 2)/2.30259
            res = res + p1
        print(f"El logaritmo decimal de {x:.0f} es {res:.3f}")
    print(" ")
    print("¿Desea calcular una función nuevamente?")
    reiniciar = int(input("Digite 1 para reiniciar la calculadora, digite 2 para cerrar la calculadora: "))
    if reiniciar == 1:
        print("")
    else:
        break
        