print("- - - Introduce dos números... Luego te daré todos los números pares que hay entre medias - - -")

n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))
list_num = []

print(f"Entre {n1} y {n2} están los siguientes números pares:")

for num in range(n1, n2+1):
    if num % 2 == 0:
        list_num.append(num)
print(list_num)