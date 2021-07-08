# Práctica 6. Ejercicios while y listas.
# P6E6_sgonzalez
# Escribe un programa que pida primero dos números (máximo y mínimo) y que
# después te pida números intermedios. Para terminar de escribir números,
# escribe un número que no esté comprendido entre los dos valores iniciales.
# El programa termina escribiendo la lista de números.
# Escribe un número: 6
# Escribe un número mayor que 6: 4
# 4 no es mayor que 6. Vuelve a probar: 50
# Escribe un número entre 6 y 50: 45
# Escribe otro número entre 6 y 50: 13


minimo = int(input("Introduce un número mínimo "))
maximo = int(input("Introduce un número mayor que %d " % (minimo)))
lista = []
while (maximo < minimo):
    maximo = int(
        input("%d no es mayor que %d, introduce otro número " % (maximo, minimo)))
intermedio = int(input("Introduce un número comprendido entre %d y %d "
                       % (minimo, maximo)))
while ((intermedio < maximo) and (intermedio > minimo)):
    lista.append(intermedio)
    intermedio = int(
        input("Introduce otro número comprendido entre %d y %d " % (minimo, maximo)))


print("Los números comprendidos entre %d y %d que has escrito son" %
      (minimo, maximo), *lista, sep=",")
