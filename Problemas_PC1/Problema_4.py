"""""

Problema 4:
Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos
puede ser calculada de la siguiente forma:

"""""

numero = int(input("Escribe un entero positivo, diferente de 1: "))

resultado = int(numero*(numero+1)/2)

print("La suma de los",numero,"primeros enteros positivos son:",resultado)