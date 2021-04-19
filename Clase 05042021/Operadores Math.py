import math
x = math.pi
p = math.trunc(x)
y = math.floor(x)
b = math.remainder(5,2) #más usado con integers como 5%2 que funciona igual
c = math.fmod(5,2) #Más usado con floats

print(f"El valor de Pi con decimales {x}")
print(f"El valor de Pi sin decimales usando Trunc: {p:.0f}") #no muestra decimales
print(f"El valor de Pi sin decimales usando Floor: {y:.2f}") #muesta dos decimales
print(f"El valor de 5 entre 2 usando remainder es {b}")
print(f"El valor de 5 entre 2 usando modf es {c:.0f}")
print("|||||||||||||||||||||||||||||||||||||||||||||||||")
val1 = 6
val2 = math.floor(val1)
val3 = math.trunc(val1)
print(f"El valor 1 que es 6sin decimales usando Trunc: {val2:.0f}") #no muestra decimales
print(f"El valor 1 que es 6 sin decimales usando Floor: {val3:.0f}") #muesta dos decimales
print("|||||||||||||||||||||||||||||||||||||||||||||||||")
x1 = 3.14
x1 = math.ceil(x1)
x2 = 3.5
x2 = math.ceil(x2)
x3 = 3.57
x3 = math.ceil(x3)
x4 = 3.8
x4 = math.ceil(x4)
print(f"El x1 sin decimales usando Ceil: {x1:.0f}") #no muestra decimales
print(f"El x2 sin decimales usando Ceil: {x2:.0f}") #no muestra decimales
print(f"El x3 sin decimales usando Ceil: {x3:.0f}") #no muestra decimales
print(f"El x4 sin decimales usando Ceil: {x4:.0f}") #no muestra decimales

#math.fabs() devuelve el valor absoluto 
print(math.fabs(-3.4))

x = math.fabs(-3.4)
print(x)



   
