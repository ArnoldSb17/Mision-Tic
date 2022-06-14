"""En tu carrera te has convertido muy popular con tus proyectos, 
hasta el punto de que un grupo de científicos te ha contratado para realizar 
investigaciones con respecto algunos estudios matemáticos para la cual encuentran 
necesaria la secuencia de Fibonacci. Dicha secuencia tiene numerosas aplicaciones en 
ciencias de la computación, matemática y teoría de juegos. De ella se destaca que cada 
número es la sumatoria de él mismo con el anterior empezando por 0 y 1. De esta manera:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377

Para este caso, tendrás que diseñar un programa que imprima los primeros 15 elementos 
de la secuencia, así como se muestra anteriormente, y poder cumplir tu contrato con los 
científicos.

Pista: Utiliza ciclos for!

"""

x = 0
y = 1
suma = x + y

for i in range(15):
    print(x) 
    x = y 
    y = suma
    suma = x + y 


