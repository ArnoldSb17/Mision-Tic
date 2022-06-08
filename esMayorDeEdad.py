print("\n")
print("===============================================")
print("===ES HORA DE VER SI ERES MAYOR DE EDAD O NO===")
print("===============================================")
print("\n")


edad = input("¿CUAL ES TU EDAD? ")
edad = int(edad)

if edad >= 18:
    print("Tu edad es " + str(edad) + ", eso quiere decir que eres mayor de edad.")

else:
    print("Tu edad es " + str(edad) + ", eso quiere decir que no eres mayor de edad.")    