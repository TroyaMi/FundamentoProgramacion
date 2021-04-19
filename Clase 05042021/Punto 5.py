"""Realizar un algoritmo que pida al usuario digitar un color y lo muestre, pero cuando el usuario digite el color rojo se
termine y lo indica"""  


while True:
    color = str(input("Digite el color que desea ver: "))
    if color == "rojo":
        print("El color ingresado es: "+str(color)+" y por tanto se detiene la ejecución")
        break
    print("El color ingresado es:"+str(color))
    
    
    
