"""""

Problema 3:
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta
por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el
peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y
cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el
último pedido y calcule el peso total del paquete que será enviado.

"""""

muñecas = int(input("Cuantas muñecas vendiste en un paquete: "))
payasos = int(input("Cuantas payasos vendiste en un paquete: "))

peso_muñecas = muñecas*75
peso_payasos = payasos*112

paquete = peso_muñecas + peso_payasos

print ("El peso total del paquete (gr) es:",paquete)
print (muñecas, "muñecas y",payasos,"payasos")
