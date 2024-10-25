def ConvertirSegundos(horas,minutos,segundos):
    horas_en_seg = horas * 3600
    minutos_en_seg = minutos * 60
    hora_completa_en_seg = horas_en_seg + minutos_en_seg + segundos
    print(f"\n{horas} horas, {minutos} minutos y {segundos} segundos equivale a {hora_completa_en_seg} segundos.")

def ConvertirHoraCompleta(segundos):
    seg_en_horas = segundos // 3600
    seg_en_minutos = (segundos % 3600) // 60
    seg_en_segundos = (segundos % 3600) % 60
    print(f"\n{segundos} segundos equivalen a {seg_en_horas} horas, {seg_en_minutos} minutos y {seg_en_segundos} segundos.")

while True:
    print("\n- - - Conversor horario - - -")
    print("\n[1] - Convertir a segundos")
    print("[2] - Convertir a horas, minutos y segundos")
    print("[3] - Salir")
    print("")
    
    opcion = input("Elige una opción del menú: ")

    if opcion == "1":
        while True:
            print("\nHas elegido la opción 1 - Convertir a segundos:")

            introduce_hora = input("Escribe el número de horas (o 'volver' para regresar): ")
            if introduce_hora.lower() == "volver":
                break

            try:
                introduce_hora = int(introduce_hora)
                introduce_minutos = int(input("Escribe el número de minutos: "))
                introduce_segundos = int(input("Escribe el número de segundos: "))
                ConvertirSegundos(introduce_hora,introduce_minutos,introduce_segundos)
            except ValueError:
                print("\nDebes introducir números!!")

    elif opcion == "2":
        while True:
            print("\nHas elegido la opción 2 - Convertir a horas, minutos y segundos:")

            introduce_segundos = input("Escribe el número de segundos (o 'volver' para regresar): ")
            if introduce_segundos.lower() == "volver":
                break
            
            try:
                introduce_segundos = int(introduce_segundos)
                ConvertirHoraCompleta(introduce_segundos)
            except ValueError:
                print("\nDebes introducir números!!")
    
    elif opcion == "3":
        print("\nHas elegido salir.")
        print("¡Hasta luego!")
        break
    else:
        print("\nOpción no válida. Por favor, elige una opción del 1 al 3.")