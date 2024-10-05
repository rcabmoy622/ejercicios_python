import random
print("- - - Adivina el número ;) - - -")
print("Se ha generado un número aleatorio entre 1 y 100, intenta adivinarlo. Tienes 10 intentos")
na = random.randint(1, 100)
intento = 1
while intento < 11:
    nu = int(input(f"Intento nº {intento} - Crees que es el número: "))
    if nu == na:
        print(f"Lo has acertado en {intento} intentos!! era el número: ", na)
    elif intento == 10:
        print("Vaya, no lo has acertado en 10 intentos. Era el número: ",na)
    else:
        print("No es ",nu,"- Intentalo de nuevo.")
        if na < nu:
            print("PISTA - El número es menor que ",nu)
        else:
            print("PISTA - El número es mayor que ",nu)
    intento += 1
    if nu == na:
        break