print("- - - Introduce un número... Luego te mostraré su tabla de multiplicar - - -")

n = int(input("Introduce un número: "))

print(f"La tabla de multiplicar del {n} es:")

for num in range(1, 11):
    tabla = num * n
    print(f"{n} * {num} = {tabla}")