print("- - - Vamos a mostrar el cuadrado desde 1 hasta el cuadrado un cualquier número - - -")

diccionario_numeros = {}

numero_introducido = int(input("Introduce un número: "))

for i in range(1,numero_introducido+1):
    diccionario_numeros[i] = i**2
    
print(f"La lista con los cuadrados desde 1 hasta el número introducido es: {diccionario_numeros}")