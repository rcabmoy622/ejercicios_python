print("- - - Análisis de números - - -")

numeros = []
cant_num = int(input("¿Cuántos números quieres introducir?: "))
mayor0 = 0
igual0 = 0
menor0 = 0

while len(numeros) < cant_num:
    num = int(input(f"Introduce el número nº{len(numeros)+1}: "))
    numeros.append(num)

for num_lis in numeros:
    if num_lis > 0:
        mayor0 += 1
    elif num_lis == 0:
        igual0 += 1
    elif num_lis < 0:
        menor0 += 1

print ("Hay",mayor0,"números mayores a cero")
print ("Hay",igual0,"números iguales a cero")
print ("Hay",menor0,"números menores a cero")