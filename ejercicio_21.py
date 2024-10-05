print("- - - Calculo del factorial de un número - - -")
n = int(input("Introduce un número para calcular su factorial: "))
f = 1
for i in range(1, n+1):
    f = i*f
print("El factorial de", n, "es:",f)