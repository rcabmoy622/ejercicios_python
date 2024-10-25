print("- - - Vamos a escribir centrado - - -")
print("A continuación introduce texto y se mostrará centrado:")

def EscribirCentrado(texto):
    print(cadena.center(80, " "))
    print(('=' * len(cadena)).center(80, " "))

cadena = str(input("\nIntroduce una cadena de texto: "))

EscribirCentrado(cadena)