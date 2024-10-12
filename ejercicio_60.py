print("- - - Vamos a obtener una matriz - - -")

matriz = []
filas = 1

while filas <= 5:
    valores = []
    contador = 1
    while contador <= 5:
        valor = str(input(f"\nEscribe el valor nº {contador} para la {filas}ª fila: "))
        if valor.isdigit():
            valor_int = int(valor)
            valores.append(valor_int)
            contador += 1
        else:
            print("\nDebes introducir un valor numérico: ")
    filas += 1
    matriz.append(valores)

print("\nLa matriz con los valores que has introducido es la siguiente:")
for listas_matriz in matriz:
    for elementos in listas_matriz:
        print(elementos, end=",")
    print("")