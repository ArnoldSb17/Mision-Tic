
print("\n")
print("=======================================")
print("===ES HORA DE VER CULA ES TU PUNTAJE===")
print("=======================================")
print("\n")
numeroRojos = int(input("Ingrese la cantidad de rojos derribados: "))
numeroVerdes = int(input("Ingrese la cantidad de verdes derribados: "))
numeroAzules = int(input("Ingrese la cantidad de azules derribados: "))

puntosRojos = numeroRojos * 10
puntosVerdes = numeroVerdes * 5
puntosazules = numeroAzules * 2

PuntajesSinBonus = puntosRojos + puntosVerdes + puntosazules

bonusRojo = 0
bonusAzules = 0
bonusVerde = 0

if numeroRojos > 10:
    bonusRojo = PuntajesSinBonus*0.1

if numeroVerdes > 5: 
    bonusVerde = PuntajesSinBonus * 0.05

if numeroAzules > 2:
    bonusAzules = PuntajesSinBonus*0.02

puntajeTotal = PuntajesSinBonus + bonusAzules + bonusVerde + bonusRojo
puntajeTotal = int(puntajeTotal)

numeroderribos = numeroRojos + numeroAzules + numeroVerdes



print("La cantidad derribada es: ", numeroderribos)
print("Puntaje total", puntajeTotal)