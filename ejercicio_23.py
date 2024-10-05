print("- - - Introduce números... Luego te daré la suma y la media de todos - - -")

nu = None
numeros = []

while nu != 0:
    nu = int(input("Introduce un número: "))
    numeros.append(nu)

suma = sum(numeros)
cant_num = len(numeros)
media = sum(numeros)/len(numeros)

print("La suma de todos los números es: ",suma)
print("La media de todos los números es: ",media)