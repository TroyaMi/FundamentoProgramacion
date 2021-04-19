#Miguel Troya and Billinwg Paternina 

#programa que  permita a los estudiantes tener claro sus condiciones antes de finalizar el semestre.

print("  ¡HOLA!, POR FAVOR DIGITE LAS NOTAS REQUERIDAS.\n")

Seguimiento = float(input("  -Digite la nota de seguimiento: "))
Parcial1 = float(input("  -Digite la nota del primer parcial: "))
Parcial2 = float(input("  -Digine la nota del segundo parcial: "))

#la suma de cada nota multplicada por su respectivo porcentaje 
SumNot = Seguimiento * 30/100 + Parcial1 * 20/100 + Parcial2 * 20/100

#Si se cumple el estudiante no presentara el examen. 
if SumNot >= 3.0: 
    print(" \n  Usted no necesita presentar el examen final")
    print(" \n  SU NOTA ES: ",SumNot)

#De lo contrario el estudiante debe presentar el examen
else: 
    print(" \n  Usted debe presentar el examen final")
    print(" \n  SU NOTA ES:",SumNot)

    NotMin = (3.0 - SumNot)/0.3
    print(" \n  Su nota minima para ganar la materia es: ",NotMin)

#El estudiante pierde la materia sin importar que haga el examen
    if NotMin > 5:
      print("  \n  Lo sentimos su nota minima es mayor a 5 por lo tanto ya perdio la meteria ")



