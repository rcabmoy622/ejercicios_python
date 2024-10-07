from datetime import datetime

print("- - - Consulta el tiempo - - -")
print("")
print("[ 1 ] - Ver la hora actual")
print("[ 2 ] - Pronóstico para hoy")
print("[ 3 ] - Pronóstico para mañana")
print("[ 4 ] - Pronóstico para los próximos 7 días")
print("[ 0 ] - Salir de la aplicación")
print("")

while True:
    numero_menu = int(input("Escribe el número correspondiente con la opción del menú para seleccionarla: "))
    print("")

    if numero_menu == 1:
        print("La hora actual es:", datetime.now().time())
    elif numero_menu == 2:
        print("Hoy se prevé un tiempo espectacular:")
    elif numero_menu == 3:
        print("Mañana hará un día agradable:")
    elif numero_menu == 4:
        print("Los proximos siete días hara un tiempo magnifico:")
    elif numero_menu == 0:
        print("¡Hasta luego!")
        break
    else:
        print("Tienes que elegir una opción del menú:")
    print("")