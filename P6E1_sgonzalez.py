# Práctica 6 - EJERCICIOS WHILE Y LISTAS
# P6E1_sgonzalez
# Escribe un programa que te pida palabras y las guarde en una lista.
# Para terminar de introducir palabras, simplemente pulsa Enter. El
# programa termina escribiendo la lista de palabras.


lista = []
palabra = input("Introduce una palabra ")
while (palabra != ""):
    lista.append(palabra)
    palabra = input("Introduce una palabra más ")
print("Las palabras que has escrito son", lista)
