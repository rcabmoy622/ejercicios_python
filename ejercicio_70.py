print("- - - Vamos a mostrar los carácteres de una cadena de texto - - -")

diccionario_cadena = {}
cadena_introducida = str(input("Introduce una cadena de texto: "))

for caracter in cadena_introducida:
    if caracter in diccionario_cadena:
        diccionario_cadena[caracter] += 1
    else:
        diccionario_cadena[caracter] = 1

print("\nTenemos un diccionario que muestra la cantidad de apariciones de cada carácter de la cadena introducida:")
print(diccionario_cadena)