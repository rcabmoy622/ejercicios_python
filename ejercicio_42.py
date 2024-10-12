print("- - - Vamos a comprobar por que empieza lo que escribes - - -")
print("")
cadena_principal = input("Escribe lo que quieras: ")
print("")
subcadena = input("Escribe algo para comprobar si lo anterior que escribiste comienza por esto: ")
print("")

if cadena_principal[:len(subcadena)] == subcadena:
    print(f"Las cadenas empiezan por lo mismo, que es: {subcadena}")
else:
    print(f"Lo primero que has escrito no empieza por {subcadena}")