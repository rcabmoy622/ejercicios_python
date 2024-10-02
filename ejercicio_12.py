import math
print("- - - Calculo de la distancia de dos puntos en el plano - - -")
x1 = int(input("Escribe la coordenada x del primer punto: "))
y1 = int(input("Escribe la coordenada y del primer punto: "))
x2 = int(input("Escribe la coordenada x del segundo punto: "))
y2 = int(input("Escribe la coordenada y del segundo punto: "))
print("La distancia entre ambos puntos es: ",math.sqrt(((x2-x1)**2)+((y2-y1)**2)))