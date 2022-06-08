"""
escribimos una letra y el programa debe de decirnos si es vocal o una consonante o carácter especial (operador de pertencia)
"""

vocales = 'aeiou'
consonantes = 'bcdfghijklmnñopqrstuvwxyz'

letraIngresada = input("INGRESE SU LETRA: ")
letraIngresada = letraIngresada.lower()

resultadoVocales = letraIngresada in vocales
resultadoConsonantes = letraIngresada in consonantes

if resultadoVocales == True:
    print("El caracter que ingresaste '"+letraIngresada+"' es una vocal")

elif resultadoConsonantes == True:
    print("El caracter que ingresaste '"+letraIngresada+"' es una consonate") 

else:
    print("El caracter que ingresaste '"+letraIngresada+"' es un caracter especial o un numero")


