print("- - - Notas de alumnos - - -")

diccionario_alumnos = {}

while True:
    try:
        numero_alumnos = int(input("\nIntroduce el número de alumnos que quieres guardar: "))
        if numero_alumnos > 0:
            break
        else:
            print("Debes introducir un número positivo!!")

    except ValueError:
        print("Debes introducir un valor numérico!!")

for i in range(numero_alumnos):
    while True:
        alumno = input(f"\nIntroduce el nombre del alumno nº{i+1}: ").capitalize()

        if alumno not in diccionario_alumnos:
            diccionario_alumnos[alumno] = []

            while True:
                nota = float(input(f"Introduce notas para {alumno} (introduce un número negativo para terminar): "))

                if nota < 0:
                    break

                diccionario_alumnos[alumno].append(nota)
            break

        else:
            print(f"{alumno} ya está agregado!!")

print("")
for alumno in diccionario_alumnos.keys():
    notas_alumno = diccionario_alumnos[alumno]
    print(f"La nota media de {alumno} es: {sum(notas_alumno) / len(notas_alumno)}")