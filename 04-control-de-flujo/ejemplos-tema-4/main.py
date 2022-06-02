'''
  condicionales:
  - >
  - >=
  - ==
  - <=
  - <
  - !=
'''
'''
  lógicos:
  - and
  - or
  - xor
  - not
'''

a = 5
b = 6
c = 7
d = 8

#Ejemplos de operadores condicionales
print(a < b)
print(a <= b)
print(a == b)
print(a > b)
print(a >= b)
print(a != b)

#Ejemplo de combinaciones de operaciones (operadores condicionales y operadores lógicos)
print(a < b and c > d)
print(a < b or c > d)
print(a < b ^ c > d)
print((a < b and c > d) or (a == b and c >= d))

#Sentencias condicionales
if a >= b:
  print("if")
elif c != d:
  print ("elif")
elif a < d:
  print ("elif2")
else:
  print("else")

#Bucles condicionales
contador = 1
while contador <= 10:
  print(contador)
  if contador == 5:
    break
  contador += 1

while contador <= 10:
  contador += 1

  if contador % 2 == 0:
    print(contador)
    continue

  print("no se dispara el continue")

#Bucles for y operadores de membresía
lista = [1, 2, "hola", 'a', 78]
tupla = (3, "ey", 54, True)
for posicion in lista:
  print(posicion)

for numero in range(5):
  print(numero)

listaPalabras = ["hola", "mensaje", "adios"]
for palabra in listaPalabras:
  print("Palabra actual: ", palabra)
  if palabra == "mensaje":
    print("He encontrado la palabra mensaje")
    break

    #Esto último es un ejemplo, porque otra forma más sencilla de hacerlo sería:

if "mensaje" in listaPalabras:
  print("He encontrado la palabra mensaje")

if "albuquerque" not in listaPalabras:
  print("No existe la palabra albuquerque en la lista")

#Longitud y orden
listaNumeros = [2, 4, 1, 3]
tuplaPalabras = ("hola", "mensaje", "adios")

longitudLista = len(listaNumeros)
ordenTupla = sorted(tuplaPalabras)
ordenReverseLista = sorted(listaNumeros, reverse=True)
print(longitudLista, ordenTupla, ordenReverseLista)

#Else en un bucle for
for palabra in listaPalabras:
  if palabra == "caballo":
    print("Encuentro la palabra caballo")
    break
else:
  print("No encuentro la palabra caballo")

#Misma acción del else hecha de otra manera
encontrado = False
for palabra in listaPalabras:
  if palabra == "caballo":
    encontrado = True
    break
if encontrado:
  print("Encuentro la palabra caballo")
else:
  print("No encuentro la palabra caballo")

#Swicht hasta Python 3.9 incluido
valor = 5
if valor == 1:
  print("Valor es 1")
elif valor == 2:
  print("Valor es 2")
elif valor == 2:
  print("Valor es 3")
elif valor == 2:
  print("Valor es 4")
elif valor == 2:
  print("Valor es 5")

#Swicht desde Python 3.10 incluido
match valor:
  case 1:
    print("Valor es 1")
  case 2:
    print("Valor es 2")
  case 3:
    print("Valor es 3")
  case 4:
    print("Valor es 4")
  case 5:
    print("Valor es 5")

#pass
for palabra in listaPalabras:
  pass
