print("- - - Vamos a introducir precios y cantidades vendidas - - -")

articulos = ["Ordenador","Pantalla","Ratón","Teclado","Impresora"]
sucursales = [[], [], [], []]
lista_precio = []

for articulo in articulos:
    precio = float(input(f"\nEscribe el precio de {articulo}: "))
    lista_precio.append(precio)

for sucursal in range(4):
    print(f"\nIntroduce las cantidades vendidas en la sucursal nº{sucursal + 1}:")
    for articulo in articulos:
        cantidad_vendida = float(input(f"Cantidad vendida de {articulo}: "))
        sucursales[sucursal].append(cantidad_vendida)

print("\nLas cantidades totales de cada artículo son:")
indice = 0
for articulo in articulos:
    total = 0
    for sucursal in sucursales:
        total += sucursal[indice]
    print(f"{articulo}: {total} unidades")
    indice += 1

print(f"\nLa cantidad de artículos en la sucursal nº2 son {sum(sucursales[1])}")

ratones = sucursales[0][2]
print(f"\nLa cantidad de ratones en la sucursal nº1 son {ratones} unidades")


print("\nLa recaudacion total en cada sucursal es:")
recaudacion_total = [0, 0, 0, 0]

for i in range(4):
    for sucursal in range(4):
        recaudacion_total[sucursal] += sucursales[sucursal][i] * lista_precio[i]

for sucursal in range(4):
    print(f"Sucursal nº{sucursal + 1}: {recaudacion_total[sucursal]} €")


total_empresa = sum(recaudacion_total)
print(f"\nLa recaudacion total de la empresa son: {total_empresa}€")

mayor_recaudacion = max(recaudacion_total)
indice_mayor = recaudacion_total.index(mayor_recaudacion)
print(f"\nLa sucursal con mayor recaudación es la sucursal nº{indice_mayor + 1} con {mayor_recaudacion} €.")