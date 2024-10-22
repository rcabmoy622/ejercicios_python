print("- - - Vamos a logearnos - - -")
print("A continuación tienes que introducir el usuario y contraseña correctos:")

intentos = 1

def Login(usuario, contrasena):
    if usuario == "usuario1" and contrasena == "asdasd":
        print("\nTe has logeado exitosamente!!!")
        return True
    else:
        return False

while intentos <= 4:
    usuario = str(input("\nIntroduce el usuario: "))
    contrasena = str(input("Introduce la contraseña: "))
    
    if Login(usuario, contrasena):
        break
    else:
        intentos += 1
        if intentos < 4:
            print(f"\nVuelve a intentarlo. Intento {intentos}/3")
    
    if intentos == 4:
        print("\nHas fallado los tres intentos de logeo!!. Saliendo...")
        break