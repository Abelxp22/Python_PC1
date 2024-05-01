"""""

Problema 2:
En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
dejar como propina.

"""""

consumo = int(input("Cuanto fue su consumo en el restaurante:"))
porcentaje_propina = int(input("Que porcentaje de propina desea dejar en (%):"))

propina = int(consumo*porcentaje_propina/100)

print("La cantidad de propina que deja es:",propina)

