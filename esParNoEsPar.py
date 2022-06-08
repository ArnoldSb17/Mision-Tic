"""
print("\n")
print("==================================================")
print("===ES HORA DE SABER SI TU NUMERO ES PAR O INPAR===")
print("==================================================")
print("\n")

numeroIngresado = int(input("Ingresa tu numero: "))
print("\n")

if (numeroIngresado % 2 == 0):
    print("El numero " + str(numeroIngresado) + ", es par!!!")
    print("\n")

else:
    print("El numero " + str(numeroIngresado) + ", es impar!!!")
    print("\n")

"""
numero = int(input("Ingrese cualquier numero: "))
final = numero + 20
while numero < final:
    numero += 1
    if numero % 2 == 0:
        print( numero )



        numero += 1
    if (numero % 3 == 0) and (numero % 5 ==0):
        print("3 5")
        numero +=1

    else:
        numero +=1