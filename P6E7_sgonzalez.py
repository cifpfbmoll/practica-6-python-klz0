# Práctica 6. Ejercicios while y listas.
# P6E7_sgonzalez
# Escribe un programa que pida un número (límite) y luego te pida números hasta
# que la suma de los números introducidos supere el límite inicial. El programa
# termina escribiendo la lista de números.
# Escribe límite: 50
# Escribe un valor: 10
# Escribe otro valor: 25
# Escribe otro valor: 7
# Escribe otro valor: 14
# El límite a superar es 50. La lista creada es 10, 25, 7, 14 ya que la suma de
# estos números es: 56

limite = int(input("Escribe el límite "))
lista = []
valor = int(input("Escribe un valor "))
lista.append(valor)
suma = valor
while (suma < limite):
    valor = int(input("Introduce otro valor "))
    lista.append(valor)
    suma += valor
print("El límite a superar es %d." %
      (limite), "La lista creada es", *lista, sep=",", end=",")
print(" la suma de estos números es %d" % (suma))
