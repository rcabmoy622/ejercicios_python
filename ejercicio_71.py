print("- - - Consultar el precio de la fruta - - -")

diccionario_frutas = {
    "platano":0.6,
    "naranja":0.5,
    "manzana":0.6,
    "pera":0.5,
    "sandía":1,
    "kiwi":0.3,
    "melon":1,
    "piña":1.5,
    "uvas":0.2,
}

print(f"Las frutas disponibles son: {diccionario_frutas.keys()}")

salir = 1

while salir != 0:
    fruta_introducida = input("Introduce una fruta: ")

    if salir == 0:
        break

    if fruta_introducida in diccionario_frutas:
        cantidad_introducida = float(input("Introduce la cantidad vendida: "))
        precio = cantidad_introducida * diccionario_frutas[fruta_introducida]
        print(f"El precio es de: {precio} €")
    else:
        print("Introduce una fruta de la lista!!")

    print("\n¿Quieres salir o realizar otra consulta?: ")
    opcion_salir = int(input("Escribe 0 para salir o 1 para continuar: "))