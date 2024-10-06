print("- - - Introduce un intervalo... Luego introducirás números y te mostraré información variada - - -")

li = int(input("Introduce el límite inferior del intervalo: "))
ls = int(input("Introduce el límite superior del intervalo: "))
num = ""
list_num = []
suma = 0
fuera = 0
num_igual = []

while li > ls:
    print("El límite inferior no puede ser mayor al límite superior. Vuelve a introducirlos:")
    li = int(input("Introduce el límite inferior del intervalo: "))
    ls = int(input("Introduce el límite superior del intervalo: "))

intervalo = range(li,ls)

while num != 0:
    num = int(input("Ahora introduce números ('0' para salir): "))
    list_num.append(num)

for n in list_num:
    if li < n < ls:
        suma += n
    else:
        fuera += 1
    
    if n == li or n == ls:
        num_igual.append(n)
        
print(f"Suma de los números dentro del intervalo: {suma}")
print(f"Números fuera del intervalo: {fuera}")
print(f"Números iguales a los límites del intervalo: {num_igual}")