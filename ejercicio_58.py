print("- - - Vamos a guardar información sobre alumno - - -")

alumnos = []
edades = []
alumnos_mayores_edad = []
mayores = []

while True:
    alumno = (input("\nEscribe el nombre de un alumno (* para salir): "))
    
    if alumno == "*":
        print("\n¡Hasta luego!")
        break

    edad = (int(input(f"\nEscribe la edad de {alumno}: ")))
    alumnos.append(alumno)
    edades.append(edad)

    if edad >= 18:
        alumnos_mayores_edad.append(alumno)  

for i in range(3):
    mayor_edad = max(edades)
    indice_mayor_edad = edades.index(mayor_edad)
    mayores.append(alumnos[indice_mayor_edad])
    edades.remove(mayor_edad)
    alumnos.pop(indice_mayor_edad)

print("\nAhora vamos a ver algunos datos relevantes:")
print(f"Los alumnos mayores de edad son: {alumnos_mayores_edad}")
print(f"Los alumnos mayores son: {mayores}")