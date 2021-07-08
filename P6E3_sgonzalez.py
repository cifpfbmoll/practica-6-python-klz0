# Práctica 6 - EJERCICIOS WHILE Y LISTAS
# P6E3_sgonzalez
# Escribe un programa que pida notas y las guarde en una lista. Para
# terminar de introducir notas, escribe una nota que no esté entre 1
# y 10. El programa termina escribiendo la lista de notas.

lista = []
nota = (float(input("Introduce una nota ")))
print("Para dejar de introducir calificaciones escribe una nota por debajo de \
1 o por encima de 10")
while ((nota <= 10) and (nota >= 1)):
    lista.append(nota)
    nota = (float(input("Introduce otra nota ")))
print("Las notas que has escrito son", lista)
