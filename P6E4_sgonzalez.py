# Práctica 6 - EJERCICIOS WHILE Y LISTAS
# P6E4_sgonzalez
# Escribe un programa que te pida dos números, de manera que el segundo sea
# mayor que el primero. El programa termina escribiendo los dos números tal y
# como se pide:
#
# Escribe un número: 6
# Escribe un número mayor que 6: 6
# 6 no es mayor que 6. Vuelve a introducir un número: 1
# 1 no es mayor que 6. Vuelve a introducir un número: 8
# Los números que has escrito son 6 y 8


numero1 = int(input("Introduce un numero "))
numero2 = int(input("Introduce otro numero "))

while (numero2 <= numero1):
    numero2 = int(input(
        "%d no es mayor que %d, vuelve a escribir otro numero " % (numero2, numero1)))

print("Has escrito los números %d y %d" % (numero1, numero2))
