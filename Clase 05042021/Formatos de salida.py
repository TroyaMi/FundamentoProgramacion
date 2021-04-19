class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
print(bcolors.FAIL + "Te acabas de equivocar"+ bcolors.ENDC)
opc = int(input(bcolors.FAIL + "Te acabas de equivocar: "+ bcolors.ENDC))
print(bcolors.OKBLUE + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)

variable = 1.23456789

print(f"el valor sin decimales es {variable:.0f}") #muestra el número sin decimales
print(f"el valor con dos decimales es {variable:.02f}") #muestra el número con 2 decimales
print(f"El valor de la factura fue {variable}")