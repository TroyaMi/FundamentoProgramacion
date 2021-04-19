#Miguel Troya and Billinwg Paternina

print("   CONVERSION DE UNIDADES DE MEDIDAS \n")
print("   Seleccione una unidad de medida \n")

#Para poder convertir de una unidad de medida a otra, es neserario seleccionar una opcion
UnidMedida = int(input(" Digite la opcion 1: Longitud. \n Digite la opcion 2: Masa.\n Digite la opcion 3: Volumen: ")) 

#Longitud
print("   Seleccione la unidad que desea convertir")
if UnidMedida == 1:
     Longitud = float(input("Digite 1: Metros a Kilometros.\nDigite 2: Millas a Pies. \nDigite 3: Pulgada a Centimetros:"))


     if Longitud == 1:
         Metros = float(input("Digite cuento metros desea convertir: "))
         m = 1000
         km = (Metros*1/m)
         print("El total de kilometros es: ",km,"Km")

     if Longitud == 2:
         Millas = float(input("Digite cuantas millas desea convertir: "))
         pies = 5280
         ps = (Millas*pies/1)
         print("Las Millas equivalen a : ",ps,"Pies")

     elif Longitud == 3: 
         Plgada = float(input("Digite cuantas pulgadas desea convertir: "))
         cm= 2.54
         centimetros = (Plgada*cm/1)
         print("La pulgada equivale a: ",centimetros,"cm")

     else:
        print("La opcion insertada no es valida ")       

#Masa     
if UnidMedida == 2:
    Masa = float(input("Digite 1: Kilogramos a Libras.\n Digite 2: Onzas a gramos.\n Digite 3: Toneladas a kilogramos: "))

    if Masa == 1:
        Kilogramos = float(input("Digite cuantos Kilogramos desea convertir: "))
        lb = 2.205
        libras = (Kilogramos*lb/1)
        print("El kilogramo dado equivale a: ",libras,"Libras")

    if Masa == 2:
         Onzas = float(input(" Digite las Onzas que desea convertir: ")) 
         gr = 28.35
         gramos =(Onzas*gr/1)
         print("Las Onzas dadas equivale a:",gramos,"gr")
        
    if Masa == 3:
        Toneladas = float(input("Digite las Toneladas que desea convertir: "))
        kgr = 1000
        Kgramo = (Toneladas*kgr/1)
        print("Las Toneladas dadas equivalen a: ",Kgramo,"Kg")

    else:
        print("La opcion insertada no es valida ")      

#Volumen
if UnidMedida == 3:
    Volumen = float(input("Digite 1: Metros cúbicos a litros.\n Digite 2: De litros a metros cúbicos: "))

    if Volumen == 1:
        MetCubicos = float(input("Digite los metros cubicos que desea convertir: "))
        ltr = 1000
        litros = (MetCubicos*ltr/1)
        print("Los metros cubicos dados equivalen a: ",litros,"litros")

    if Volumen == 2:
        Ltros = float(input("Digite los Litros que desea convertir: "))
        Mc = 1000
        MCubicos = (Ltros*Mc/1)
        print("Los Litros dados equivalen a: ",MCubicos,"Metro cubico")

    else:
        print("La opcion insertada no es valida ")  

else:
    print("La opcion insertada no es valida ")  



       


     

     
