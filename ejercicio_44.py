print("\n- - - Vamos a contar las palabras de lo que escribes - - -")
cadena = input("\nEscribe lo que quieras: ")
palabras = cadena.split()
contador_palabras = 0

for palabra in palabras:
    contador_palabras += 1
print(f"\nLo que has escrito tiene {contador_palabras} palabras.")