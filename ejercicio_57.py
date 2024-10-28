lista1 = []
lista2 = []
lista3 = []

for i in range(1,6):
    valor_lista1 = int(input(f"Introduce el valor nº {i} para la lista 1: "))
    lista1.append(valor_lista1)

print("")

for i in range(1,6):
    valor_lista2 = int(input(f"Introduce el valor nº {i} para la lista 2: "))
    lista2.append(valor_lista2)

for i in range(5):
	lista3.append(lista1[i]+lista2[i])

print(f"\nLa suma de las dos listas es: {lista3}")