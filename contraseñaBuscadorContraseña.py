"""
variable que almacene un string.
string va ser una contraseña.
vamos a recibir contraseñas que seran comapradas.
con esta contraseña previamente guardada.
el usuario tendra 3 intentos.
si es correcto imprimir "Adelante" y fin del programa.
de lo contrario " indicarle el numero de intentos".
despues de tres fallos, imprimir "se bloqueo la cuenta" fin del progrma.
"""
import os

__contraseña = "5489"
interface = """
----------------------
! Usuario 5468554 !
! contraseña **** !
----------------------
"""

c = 0
while c < 3:
    os.system("cls")  
    print( interface )
    contraseña = input("Ingrese una contraseña: ")
    if contraseña == __contraseña:
        print("Adelante")
        c = 3
    else:
        c += 1
        print(f"Le quedan {3 - c} intentos" )
        if c == 3:
            print("se bloqueo la cuenta" )
            input()


"""
Buscador de contraseña 
"""

"""
bandera = True
c = 0
while bandera:
    if str( c ) == __contraseña:
        bandera = False
    print( c )
    c += 1
print( c )
input()
"""