print("- - - Programa con menú - - -")

lista_numeros = [0,1,2,3,4,5,6,7,8,9]

opcion = ""

while True:
    print("\n- - - Opciones - - -")
    print("[1] - Añadir un número a la lista")
    print("[2] - Añadir un número a la lista en una posición")
    print("[3] - Longitud de la lista")
    print("[4] - Eliminar el último número")
    print("[5] - Eliminar un número")
    print("[6] - Contar números")
    print("[7] - Posiciones de un número")
    print("[8] - Mostrar números")
    print("[9] - Salir")
    print("")
    
    opcion = input("Elige una opción del menú: ")

    if opcion == "1":
        while True:
            print("\nHas elegido la opción 1 - Añadir un número a la lista:")
            print(f"Esta es la lista: {lista_numeros}")

            opcion1 = int(input("Escribe un número de la lista para añadirlo al final de esta (-1 para volver al inicio): "))

            if opcion1 == -1:
                break

            if opcion1 in lista_numeros:
                lista_numeros.append(opcion1)
                print("\nNúmero añadido correctamente!!")
            else:
                print("\nDebes introducir un valor de la lista!!")

    elif opcion == "2":
        while True:
            print("\nHas elegido la opción 2 - Añadir un número a la lista en una posición:")
            print(f"Esta es la lista: {lista_numeros}")

            posicion_opcion2 = int(input("Elige una posicion (-1 para volver al inicio): "))

            if posicion_opcion2 == -1:
                break
            
            opcion2 = int(input("Escribe un número de la lista para añadirlo en la posición elegida: "))
            if opcion2 in lista_numeros:
                lista_numeros.insert(posicion_opcion2, opcion2)
                print(f"\nNúmero añadido correctamente en la posición {posicion_opcion2}!!")
            else:
                print("\nDebes introducir un valor de la lista!!")
    
    elif opcion == "3":
        while True:
            print("\nHas elegido la opción 3 - Longitud de la lista:")
            print(f"\nLa lista actualmente tiene una longitud de {len(lista_numeros)} números.")

            opcion3 = int(input("Escribe -1 para volver al inicio: "))
            if opcion3 == -1:
                break

    elif opcion == "4":
        while True:
            print("\nHas elegido la opción 4 - Eliminar el último número:")

            opcion4 = int(input("Escribe 0 para borrar el último número de la lista (-1 para volver al inicio): "))
            if opcion4 == 0:
                ultimo_numero = lista_numeros.pop()
            print(f"\nHas eliminado el número {ultimo_numero} de la lista.")
            print(lista_numeros)

            if opcion4 == -1:
                break

    elif opcion == "5":
        while True:
            print("\nHas elegido la opción 5 - Eliminar un número:")
            print(f"Esta es la lista: {lista_numeros}")

            posicion_opcion5 = int(input("Elige una posicion a partir de la 1 para eliminarla (-1 para volver al inicio): "))

            if posicion_opcion5 == -1:
                break
            
            if posicion_opcion5 in lista_numeros[1:]:
                lista_numeros.remove(posicion_opcion5)
                print(f"\nNúmero elimininado correctamente de la posición {posicion_opcion5}!!")
            else:
                print("\nDebes introducir una posición de la lista!!")

    elif opcion == "6":
        while True:
            print("\nHas elegido la opción 6 - Contar números:")

            opcion6 = int(input("Elige una número para contar cuantas veces aparece en la lista (-1 para volver al inicio): "))

            if opcion6 == -1:
                break
            
            if opcion6 in lista_numeros:
                apariciones_opcion6 = lista_numeros.count(opcion6)
                print(f"\nEl número {opcion6} aparece {apariciones_opcion6} veces en la lista!!")
            else:
                print("\nDebes introducir una posición de la lista!!")

    elif opcion == "7":
        while True:
            print("\nHas elegido la opción 7 - Posiciones de un número:")

            opcion7 = int(input("Elige un número para ver sus posiciones a partir de la 1 (-1 para volver al inicio): "))

            if opcion7 == -1:
                break
            
            if opcion7 in lista_numeros:
                posiciones = []
                for cada_posicion in range(len(lista_numeros)):
                    if lista_numeros[cada_posicion] == opcion7:
                        posiciones.append(cada_posicion + 1)
                print(f"\nEl número {opcion7} está en la/s posición/es {posiciones} de la lista!!")
            else:
                print("\nDebes introducir una posición de la lista!!")

    elif opcion == "8":
        while True:
            print("\nHas elegido la opción 8:")
            print(f"Los números de la lista son {lista_numeros}")

            opcion8 = int(input("\nEscribe -1 para volver al inicio: "))

            if opcion8 == -1:
                break


    elif opcion == "9":
        print("\nHas elegido salir.")
        print("¡Hasta luego!")
        break
    else:
        print("\nOpción no válida. Por favor, elige una opción del 1 al 9.")