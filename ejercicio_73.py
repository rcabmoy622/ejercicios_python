diccionario_agenda = {"Edmundo":123456789, "Casandra":987654321}
opcion = ""

while True:
    print("\n- - - Agenda - - -")
    print("[1] - Añadir/modificar")
    print("[2] - Buscar")
    print("[3] - Borrar")
    print("[4] - Listar")
    print("[5] - Salir")
    print("")
    
    opcion = input("Elige una opción del menú: ")

    if opcion == "1":
        while True:
            print("\nHas elegido la opción 1 - Añadir o modificar:")

            comprobar_nombre = str(input("Escribe un nombre para comprobar si está agendado (o 'volver' para regresar): ")).capitalize()
            if comprobar_nombre == "Volver":
                break

            if comprobar_nombre in diccionario_agenda:
                print(f"\nEl teléfono de {comprobar_nombre} es {diccionario_agenda[comprobar_nombre]}")

                while True:
                    pregunta_modificar = str(input("¿Quieres modificarlo? (escribe 'si' o 'no'): "))
                    if pregunta_modificar == "si":
                        corregir_teléfono = int(input("Escribe el teléfono corregido: "))
                        diccionario_agenda[comprobar_nombre] = corregir_teléfono
                        print(f"\nEl teléfono de {comprobar_nombre} ahora es {corregir_teléfono}!!")
                        break
                    elif pregunta_modificar == "no":
                        print("No se realizarán modificaciones")
                        break
                    else:
                        print("Opción no válida!! Escribe 'si' para modificarlo o 'no' para no realizar modificaciones")

            elif comprobar_nombre not in diccionario_agenda:
                agregar_teléfono = int(input("Contacto no encontrado!! A continuación, agrega su teléfono: "))
                diccionario_agenda[comprobar_nombre] = agregar_teléfono
                print(f"Has agregado a {comprobar_nombre} a la agenda!!")

    elif opcion == "2":
        while True:
            print("\nHas elegido la opción 2 - Buscar:")

            buscar_nombre = str(input("\nEscribe un nombre para buscarlo (o 'volver' para regresar): ")).capitalize()
            if buscar_nombre == "Volver":
                break


            empieza_por_buscar_nombre = [nombre for nombre in diccionario_agenda.keys() if nombre.startswith(buscar_nombre)]
            
            if empieza_por_buscar_nombre:
                print(f"Los siguientes contactos empiezan por '{buscar_nombre}': {empieza_por_buscar_nombre}")
            else:
                print(f"No hay ningún contacto que empiece por '{buscar_nombre}'.")
    
    elif opcion == "3":
        while True:
            print("\nHas elegido la opción 3 - Borrar:")

            buscar_nombre = str(input("Escribe un nombre para buscarlo (o 'volver' para regresar): ")).capitalize()
            if buscar_nombre == "Volver":
                break

            if buscar_nombre in diccionario_agenda:
                pregunta_borrar = str(input(f"\nEl contacto {buscar_nombre} está en la agenda. ¿Quieres borrarlo? (escribe si o no): "))
                if pregunta_borrar == "si":
                    del diccionario_agenda[buscar_nombre]
                    print(f"Se ha eliminado a {buscar_nombre} de la agenda.")
                elif pregunta_borrar == "no":
                    print("No se realizarán modificaciones")
                else:
                    print("Opción no válida!! Escribe 'si' para modificarlo o 'no' para no realizar modificaciones")
            else:
                print(f"No se ha encontrado a {buscar_nombre} en la agenda")

    elif opcion == "4":
        while True:
            print("\nHas elegido la opción 4 - Listar:")

            print("\nTienes a los siguientes contactos en la agenda:")
            print("")
            for nombre, telefono in diccionario_agenda.items():
                print([nombre, telefono])
            
            volver = str(input("\nEscribe 'volver' para regresar): "))
            if volver == "volver":
                break

    elif opcion == "5":
        print("\nHas elegido salir.")
        print("¡Hasta luego!")
        break
    else:
        print("\nOpción no válida. Por favor, elige una opción del 1 al 5.")