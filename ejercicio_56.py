print("- - - Vamos a obtener los días de cada mes - - -")

meses = ["","Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias_meses = ["",31,28,31,30,31,30,31,31,30,31,30,31]

while True:
    mes = int(input("\nEscribe el nº de un mes (0 para salir): "))
    numero_mes = int(mes)
    if 1 <= mes <= 12:
        print(f"{meses[numero_mes]} tiene {dias_meses[numero_mes]} días")

    elif mes == 0:
        print("\n¡Hasta luego!")
        break
        
    else:
        print("\nDebes introducir un valor entre 0 y 12 ")