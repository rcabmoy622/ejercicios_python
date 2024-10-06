print("- - - Tablas de multiplicar del 1, 2, 3, 4 y 5: - - -")

lista =  [1,2,3,4,5]

while True:
    n = int(input("Introduce el número de la tabla que quieres ver: "))

    if n in lista:
        print(f"La tabla de multiplicar del {n} es:")
        for num in range(1, 11):
            tabla = num * n
            print(f"{n} * {num} = {tabla}")
    else:
        print("Tienes que introducir un número del 1 al 5.")