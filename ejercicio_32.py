print("- - - Calculadora de ahorro anual - - -")
print("")
print("Con esta utilidad puedes introducir la cantidad que depositarás cada mes para determinar cuánto ahorrarás en un año.")
print("También puedes saber cuanto llevas ahorrado cada mes.")
print("")

año = int(input(f"Introduce el año para realizar el cálculo: "))
print("")

meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
deposito_realizado = []

for mes in meses:
    deposito_mes = int(input(f"Introduce el deposito de {mes}: "))
    deposito_realizado.append(deposito_mes)

ahorro_total = sum(deposito_realizado)

print(f"Si en cada mes depositas las cantidades que has indicado, en {año} habrás ahorrado {ahorro_total} € ")
print("")
print("Puedes consultar el deposito que has introducido para cada mes escribiendo el nombre del mes (pulsa 0 para salir):")
print("")

while True:
    consulta_mes = input("Introduce un mes: ").capitalize()
    print("")
   
    if consulta_mes in meses:
        numero_mes = meses.index(consulta_mes)
        print(f"El depósito realizado en {consulta_mes} es de {deposito_realizado[numero_mes]} €")
        print("")
    else:
        print("Introduce un mes válido")
        print("")

    if consulta_mes == '0':
        print("¡Hasta luego!")
        print("")
        break