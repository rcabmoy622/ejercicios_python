print("\n- - - Vamos a mostrar las iniciales de tu nombre en mayúsculas - - -")
cadena = input("\nEscribe tu nombre y apellidos: ")
palabras = cadena.split()
iniciales_nombre = []
cadena_iniciales = ""

for palabra in palabras:
    primera_letra = palabra[0].upper()
    iniciales_nombre.append(primera_letra)

for inicial in iniciales_nombre:
    cadena_iniciales += str(inicial)

print(f"\nLas iniciales de tu nombre son: {cadena_iniciales}.")