# Práctica 6 - EJERCICIOS WHILE Y LISTAS
# P6E2_sgonzalez
# Escribe un programa que te pida números y los guarde en una lista.
# Para terminar de introducir número, simplemente escribe "Salir".
# El programa termina escribiendo la lista de números.

lista = []
numero = int(input("Escribe un número "))
print("Cuando hayas acabado de escribir números, escribe salir \
para finalizar")

while (numero != "salir"):
    lista.append(numero)
    numero = input("Escribe otro numero ")

print("Los números que has escrito son ", lista)
