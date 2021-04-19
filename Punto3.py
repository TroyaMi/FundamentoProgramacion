#Miguel Troya and Billinwg Paternina

#programa que le permita revisar si dado un punto en el plano cartesiano e informe si se encuentra en el origen, o sobre un eje específico o en un cuadrante y cuál.
print("   *PUNTOS EN EL PLANO CARTESIANO*   \n ")

Punto_X = float(input("    Digite el valor del punto X: "))
Punto_Y = float(input("    Digite el valor del punto Y: "))


PuntPlano = Punto_X,Punto_Y


#Dados los puntos de 0 en X y Y determinamos el origen del plano
if Punto_X == 0 and Punto_Y == 0:
    print("    Los puntos",PuntPlano,"Se encuentran el el origen del palno")

#Segun los valores de los putnos x,y se determina en que cuadrante pertenece 
if Punto_X > 0 and Punto_Y > 0: 
    print("    Los puntos",PuntPlano,"Se encuentra en el cuadrante 1")

if Punto_X < 0 and Punto_Y > 0:
    print("    los puntos",PuntPlano,"Se encuentran en el cuadrante 2")

if Punto_X < 0 and Punto_Y < 0:
    print("    Los puntos",PuntPlano,"Se encuentran en el cuadrante 3")

if Punto_X > 0 and Punto_Y < 0:
    print("    Los puntos",PuntPlano,"Se encuentran en el cuadrante 4")

#Dados los puntos de 0 en X y Y, determinamos cual pertenece al eje Y
if Punto_X == 0 and Punto_Y > 0:
    print("    Los puntos",PuntPlano,"Se encuentran en el eje Y del plano")

if Punto_X == 0 and Punto_Y < 0:
    print("    Los puntos",PuntPlano,"Se encuentran en el eje Y del plano")

#Dados los puntos de 0 en X y Y, determinamos cual pertenece al eje X
if Punto_X > 0 and Punto_Y == 0:
    print("    Los puntos",PuntPlano,"Se encuentran en el eje X del plano")

if Punto_X < 0 and Punto_Y == 0:
    print("    Los puntos",PuntPlano,"Se encuentran en el eje X del palno")


