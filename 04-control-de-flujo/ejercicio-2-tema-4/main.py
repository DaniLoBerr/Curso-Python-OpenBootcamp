print("Calcule los números impares existentes entre dos números")

numeroInicial = int(input("Introduzca un número inicial: "))
numeroFinal = int(input("Introduzca un número final: "))
numerosImpares = []

if numeroInicial > numeroFinal:
  print("Error: Introduzca un número inicial menor que el final")

while numeroInicial <= numeroFinal:
  if numeroFinal % 2 != 0:
    numerosImpares.append(numeroFinal)
  numeroFinal -= 1

numerosImpares = sorted(numerosImpares)

print("Los números impares existentes entre los números proporcionados son:", numerosImpares)
