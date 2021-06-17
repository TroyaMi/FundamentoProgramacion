#Adivinar un número de cuatro dígitos diferentes. Picas y Fijas. Pica es un dígito que está en el original pero
#no en la misma posición, y las fijas son las que están en la misma posición y con el mismo valor
import os

num = input("Digite un número de cuatro dígitos diferentes: ")
os.system("cls")

int = 0
while True:
    int = int + 1
    numJug = input("Señor jugador, digite el número: ")
    nf = 0
    np = 0
    for i in range(0,len(numJug)): #se descompone el número del jugador para compararlo con cada dígito del número a adivinar"
        digJug = numJug[i:i+1]
        for j in range(0,len(num)):
            dig = num[j:j+1]
            #f1 = False
            #f2 = False
            if dig == digJug and i == j:
                nf = nf + 1
            if dig == digJug and i != j:
                np = np + 1
    print(f"INTENTO {int}")            
    print(f"El número de fijas es: {nf}")
    print(f"El número de picas es: {np}") 
    respu = input("Desea continuar? 1 para seguir, 2 para salir: ")
    if respu == "2":
        break
