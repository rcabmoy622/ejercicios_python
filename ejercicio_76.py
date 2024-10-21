print("- - - Comprobar si son múltiplos - - -")
print("A continuación vas a introducir dos números enteros, y te diré si alguno de ellos es múltiplo del otro")

def EsMultiplo(numero_a,numero_b):
    primera_operacion = a % b
    segunda_operacion = b % a
    
    if primera_operacion == 0:
        print(f"\nEl número 'a' ({a}) es mútiplo del número 'b' ({b}).")
    elif segunda_operacion == 0:
        print(f"\nEl número 'b' ({b}) es mútiplo del número 'a' ({a}).")
    else:
        print("\nNingúno de los dos números es mútiplo del otro")

a = int(input("\nIntroduce el número 'a': "))
b = int(input("Introduce el número 'b': "))

EsMultiplo(a,b)

# En la función, en los dos casos comprobamos si el resultado es cero porque para que un número sea múltiplo de otro
# el resultado del módulo debe ser cero.