lista_original = []
lista_sin_duplicados = []

for i in range(1,10**10):
    valor_introducido = int(input(f"Introduce el valor nº{i} a la lista (introduce uno negativo para salir): "))
    lista_original.append(valor_introducido)
    if valor_introducido < 0:
        lista_original.pop()
        break

print(f"\nLa lista original es esta: {lista_original}")
print("\nVamos a eliminar los valores duplicados de la lista...")

for i in lista_original:
    if i not in lista_sin_duplicados:
        lista_sin_duplicados.append(i)

print(f"\nLa lista sin valores duplicados es esta: {lista_sin_duplicados}")