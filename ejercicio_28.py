print("- - - Introduce un intervalo... Luego introducirás números y te mostraré información variada - - -")

limite_inferior = int(input("Introduce el límite inferior del intervalo: "))
limite_superior = int(input("Introduce el límite superior del intervalo: "))
numero_introducido = ""
lista_numeros_introducidos = []
suma_valores_del_rango = 0
cantidad_numeros_fuera = 0
numeros_igual_al_limite = []

while limite_inferior > limite_superior:
    print("El límite inferior no puede ser mayor al límite superior. Vuelve a introducirlos:")
    limite_inferior = int(input("Introduce el límite inferior del intervalo: "))
    limite_superior = int(input("Introduce el límite superior del intervalo: "))

while numero_introducido != 0:
    numero_introducido = int(input("Ahora introduce números ('0' para salir): "))
    lista_numeros_introducidos.append(numero_introducido)

for numero_evaluado in lista_numeros_introducidos:
    if limite_inferior < numero_evaluado < limite_superior:
        suma_valores_del_rango += numero_evaluado
    else:
        cantidad_numeros_fuera += 1

    if (numero_evaluado == limite_inferior) or (numero_evaluado == limite_superior):
        numeros_igual_al_limite.append(numero_evaluado)
        
print(f"Suma de los números dentro del intervalo: {suma_valores_del_rango}")
print(f"Números fuera del intervalo: {cantidad_numeros_fuera}")
print(f"Números iguales a los límites del intervalo: {numeros_igual_al_limite}")