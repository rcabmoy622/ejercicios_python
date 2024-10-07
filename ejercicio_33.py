print("- - - Calculadora de horas trabajadas y sueldo - - -")
print("")
print("Con esta utilidad puedes calcular el total de horas semanales trabajadas y el sueldo correspondiente.")
print("")

primer_dia = int(input("Introduce el primer día de la semana para realizar el cálculo: "))
ultimo_dia = int(input("Introduce el último día de la semana para realizar el cálculo: "))
mes = str(input(f"Introduce el mes para realizar el cálculo: "))
sueldo_hora = int(input("Introduce el sueldo que cobras por hora: "))
print("")

dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sábado"]
lista_horas = []

for dia in dias:
    horas_un_dia = int(input(f"Introduce las horas trabajadas el {dia}: "))
    lista_horas.append(horas_un_dia)

horas_totales = sum(lista_horas)
sueldo = sueldo_hora * horas_totales

print("")
print(f"En la semana del {primer_dia} al {ultimo_dia} de {mes} has trabajado un total de {horas_totales} horas ")
print("")
print(f"Te corresponden {sueldo} € por haber trabajado {horas_totales} horas durante la semana del {primer_dia} al {ultimo_dia} de {mes}.")
print("")