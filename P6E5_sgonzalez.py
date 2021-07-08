# Práctica 6. Ejercicios while y listas.
# P6E5_sgonzalez
# Escribe un programa que te pida números cada vez más grandes y que se guarden
# en una lista. Para acabar de escribir los números, escribe un número que no
# sea mayor que el anterior. El programa termina escribiendo la lista de números:
# Escribe un número: 6
# Escribe un número mayor que 6: 10
# Escribe un número mayor que 10: 12
# Escribe un número mayor que 12: 25
# Escribe un número mayor que 25: 9
# Los números que has escrito son: 6, 10, 12, 25  (Comentario si os fijáis ya
# no se imprime la lista tal cual, hay que imprimir uno por uno los valores
# de la lista, haced esto así a partir de ahora)

numero1 = int(input("Introduce un número "))
lista = []
lista.append(numero1)
numero2 = int(
    input("Introduce otro número de valor superior a %d " % (numero1)))

while (numero2 > numero1):
    lista.append(numero2)
    numero1 = numero2
    numero2 = int(
        input("Introduce otro número de valor superior a %d " % (numero1)))

print(*lista, sep=", ")
