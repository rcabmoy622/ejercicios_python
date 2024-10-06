print("- - - Análisis de caracteres - - -")

vocales = ["a","e","i","o","u"]
ca = None

while ca !=" ":
    ca = (input("Introduce un caracter: "))
    if ca in vocales:
        print("VOCAL")
    else:
        print("NO VOCAL")