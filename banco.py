"""
+ se pide el monto 
+ numero de cuotas

caso1: 
    valorInicial < 500.000
    interes del 10%
    valor inial del 3% por cuota

caso2:
    valorInicial >= 500'000 y valorInicial < 1'000'000
    interes incial del 7%
    valor incial generar un interes del 5% por cuota

caso3:
    valorIncial >= 1'000'000
    interes incial del 4%
    valor incial generar un interes del 9% por cuota

- Salidas
- ValorTotal del prestamo
- valorPorCuota

"""
print("\n")
print("=======================================")
print("===BIENVENIDO AL BANCO DE MISIÓN TIC===")
print("=======================================")
print("\n")
valorInicial = int(input("Ingresa el valor del prestamo: "))
cuotaInicil = int(input("A cuntas cuotas: "))
print("\n")

if valorInicial < 500000:
    if cuotaInicil > 1:
        interesInicil = 0.1
        interesGeneral = 0.03
        interesGeneral = int(interesGeneral)

        cuotas = valorInicial / cuotaInicil
        valorInteresInicil = valorInicial * interesInicil
        valorCuotasGeneral = cuotas * interesGeneral + cuotas
        valorCuotasInicil = (cuotas * interesInicil) + valorCuotasGeneral
        totalApagar = (valorCuotasGeneral * cuotaInicil) + valorCuotasInicil

        print("Cuota inicil: " + str(valorCuotasInicil) + "\nCuotas generales: " + str(valorCuotasGeneral) + "\nTotal a pagar: " + str(totalApagar) + "\n\n")
    
    else:
        interesInicil = 0.1
        interesGeneral = 0.03

        cuotas = valorInicial / cuotaInicil
        valorInteresInicil = valorInicial * interesInicil
        valorCuotasInicil = (cuotas * interesInicil)
        totalApagar = valorInteresInicil

        print("Cuota inicil: " + str(valorCuotasInicil) + "\nTotal a pagar: " + str(totalApagar) + "\n\n")

if ((valorInicial >= 500000) and (valorInicial < 1000000)) :
    if cuotaInicil > 1:
        interesInicil = 0.07
        interesGeneral = 0.05

        cuotas = valorInicial / cuotaInicil
        valorInteresInicil = valorInicial * interesInicil
        valorCuotasGeneral = cuotas * interesGeneral + cuotas
        valorCuotasInicil = (cuotas * interesInicil) + valorCuotasGeneral
        totalApagar = (valorCuotasGeneral * cuotaInicil) + valorCuotasInicil

        print("Cuota inicil: " + str(valorCuotasInicil) + "\nCuotas generales: " + str(valorCuotasGeneral) + "\nTotal a pagar: " + str(totalApagar) + "\n\n")

    else:
        interesInicil = 0.07
        interesGeneral = 0.05

        cuotas = valorInicial / cuotaInicil
        valorInteresInicil = valorInicial * interesInicil
        valorCuotasInicil = (cuotas * interesInicil)
        totalApagar = valorInteresInicil

        print("Cuota inicil: " + str(valorCuotasInicil) + "\nTotal a pagar: " + str(totalApagar) + "\n\n")

if valorInicial >= 1000000:
    if cuotaInicil > 1:
        interesInicil = 0.04
        interesGeneral = 0.09

        cuotas = valorInicial / cuotaInicil
        valorInteresInicil = valorInicial * interesInicil
        valorCuotasGeneral = cuotas * interesGeneral + cuotas
        valorCuotasInicil = (cuotas * interesInicil) + valorCuotasGeneral
        totalApagar = (valorCuotasGeneral * cuotaInicil) + valorCuotasInicil

        print("Cuota inicil: " + str(valorCuotasInicil) + "\nCuotas generales: " + str(valorCuotasGeneral) + "\nTotal a pagar: " + str(totalApagar) + "\n\n")

    else:
        interesInicil = 0.1
        interesGeneral = 0.03

        cuotas = valorInicial / cuotaInicil
        valorInteresInicil = valorInicial * interesInicil
        valorCuotasInicil = (cuotas * interesInicil)
        totalApagar = valorInteresInicil

        print("Cuota inicil: " + str(valorCuotasInicil) + "\nTotal a pagar: " + str(totalApagar) + "\n\n")




