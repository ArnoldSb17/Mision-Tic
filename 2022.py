from turtle import clear
from xml.etree.ElementPath import ops
import os 


interface = """
-------------------------------

\t\t\tCalculadora

opciones:
[A]dicion
[R]esta
[M]ultiplicacion
[D]ivision

[S]alida

-------------------------------
"""

bandera = True
while bandera:
    os.system("cls")

    print( interface )
    opc = input("Ingrese una opcion: ").upper()
    print("-------------------------------")

    if opc == 'S':
        print("Adios")
        bandera = False
    else:
        x = float(input("valor1: "))
        y = float(input("valor2: "))
        if opc == 'A':
            print("\t\t\tSuma") 
            z = x + y
            if z % 1 == 0:
                z = int(z)  
                print(f"{x} + {y} = { z }")
                input()
        elif opc == 'R':
            print("\t\t\tResta")   
            print(f"{x} - {y} = { x - y }")   
            input()   
        elif opc == 'M':
            print("\t\t\tMultiplicacion")
            print(f"{x} * {y} = { x * y }")
            input()
                
        elif opc == 'D':
            print("\t\t\tDivision")        
            if y == 0:
                print("Indeterminado")
            else:
                print(f"{x} / {y} = { x / y }")
            input()

        else:
            print("Ha ingresa una opcion NO valida")

    input()

# import sys 
# sys.cls