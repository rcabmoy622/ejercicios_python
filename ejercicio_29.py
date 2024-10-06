print("- - - Introduce un número que haga de base y otro para ser su exponente... Luego te daré el resultado de la potencia: - - -")
b = int(input("Introduce la base: ")) 
e = int(input("Introduce el exponente: "))
r = 1

for n in range(e):
    r *= b
print(f"{b} elevado a {e} = {r}")