print("- - - Vamos a obtener información sobre tus notas - - -")

notas = []
contador = 1

while contador <= 5:
    nota = float(input(f"\nEscribe la nota nº {contador}: "))
    if 0 <= nota <= 10:
        notas.append(nota)
        contador += 1
    else:
        print("\nDebes introducir un valor entre 0 y 10 ")


media_notas = (sum(notas))/(len(notas))

print(f"\nTodas tus notas son: {notas} ")
print(f"\nTu notas media es: {media_notas} ")
print(f"\nTu nota mas alta es: {max(notas)} ")
print(f"\nTu nota mas baja es: {min(notas)} ")