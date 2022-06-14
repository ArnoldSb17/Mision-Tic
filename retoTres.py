numeroIngresado = int(input("numero: "))

if(numeroIngresado >= 0) and (numeroIngresado <= 9):
    print("unidad")

elif (numeroIngresado >= 10) and (numeroIngresado <= 99):
    print("decena")

elif (numeroIngresado >= 100) and (numeroIngresado <= 999):
    print("centena")

elif (numeroIngresado >= 1000) and (numeroIngresado <= 9999):
    print("milesima")

elif (numeroIngresado >= 10000) and (numeroIngresado <= 99999):
    print("decena de mil")

elif (numeroIngresado >= 100000) and (numeroIngresado <= 999999):
    print("centena de mil")