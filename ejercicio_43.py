print("- - - Vamos a contar un cierto carácter en lo que escribes - - -")

cadena_principal = input("\nEscribe lo que quieras: ")

caracter = input("\nEscribe un carácter para contar cuantas veces está en lo que has escrito: ")
print(f"\nEl carácter '{caracter}' esta {cadena_principal.count(caracter)} veces en la cadena '{cadena_principal}'")