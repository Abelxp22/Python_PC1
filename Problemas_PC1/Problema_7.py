"""""

Problema 7:
Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
- Mostrar una suma de los dos números
- Mostrar una resta de los dos números (el primero menos el segundo)
- Mostrar una multiplicación de los dos números
- En caso de introducir una opción inválida, el programa informará de que no es correcta.

"""""


numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))

suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1*numero_2

print("Menu:")
print("1. Mostrar suma de los dos números")
print("2. Mostrar resta (primer número menos segundo número)")
print("3. Mostrar multiplicación de los dos números")
opcion = input("Elija una opción (1,2 o 3): ")


if opcion == '1':
    resultado = suma
    print("La suma de", numero_1, "y", numero_2, "es:", resultado)
elif opcion == '2':
    resultado = resta
    print("La resta de", numero_1, "menos", numero_2, "es:", resultado)
elif opcion == '3':
    resultado = multiplicacion
    print("La multiplicación de", numero_1, "por", numero_2, "es:", resultado)
else:
    print("Opción no válida. Por favor, elija una opción correcta.")
