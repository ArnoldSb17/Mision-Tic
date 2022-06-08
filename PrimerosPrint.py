print("====================BIENVENIDO AL CINE DE MISIÓN TIC ====================")
nombre = input("INGRESA TU NOMBRE: ")
edad = int(input("QUE EDAD TIENES: "))

if edad > 119:
    print("\nHola "+ nombre.capitalize() + ", Que??? tines "+ str(edad) + " años!!!!.\nCreia que la perona con mas edad es la japonesa 'Kane Tanaka' con una edad de 119 años.\n" )

elif edad >= 18:
    print("\nHola "+ nombre.capitalize() +" Usted cumple la edad minima. \nPuede entrar a ver la pelicula.\n")

elif edad < 18 and edad > 0:
    estaAcompañado = input("Esta acompañado por un adulto?:").lower()
    if estaAcompañado == "si":
        nombreAcompañante = input("Regalame el nombre de tu acompañante: ")

        print("Hola " + nombre.capitalize() +" Usted no cumple el minimo de edad pero esta acompañado por " +nombreAcompañante.capitalize() + "\nPuede entrar a ver la pelicula.\n")

    elif estaAcompañado == "no":
        print("Hola pequeño" + nombre.capitalize() +" Usted no cumple el minimo de edad y no esta acompañado por un adulto.\nNo puede pasar a ver la pelicula.\n")
else:
    print("\nHola!! "+ nombre + "\nSi sabes que no puedes tener una edad negativa. \n"+ str(edad) + " esa no es tu edad. \n" )
