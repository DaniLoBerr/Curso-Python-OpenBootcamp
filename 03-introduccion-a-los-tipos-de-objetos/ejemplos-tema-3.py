#numero entero. Inmutable
a=1
print('El valor de mi variable a es:', a, type(a))

#string. Inmutable
b='hola'
print('El valor de mi variable b es:', b, type(b))

#boolean. Inmutable
m=True
n=False
print('El valor de mi variable m es:', m, type(m))
print('El valor de mi variable n es:', n, type(n))

#float. Inmutable
o=2.5
print('El valor de mi variable o es:', o, type(o))

#tupla. Inmutable
c=(2, 'z', 'adios')
print('El valor de mi variable c es:', c, type(c))

#lista. Mutable
d=[3, 'y', 'ey']
print('El valor de mi variable d es:', d, type(d))

#sustituciones de elementos de lista
d[1]='x'
print('Sustituyo el valor de la segunda posición de mi variable d y queda:', d)

#adiciones a lista
d.append('patata')
d.append('w')
print('Añado dos elementos más a la lista de mi variable d y queda:', d)

#eliminar elementos de listas
d.remove('ey')
print('Elimino un elemento de la lista de mi variable d y queda:', d)

#anidar lista dentro de lista
e=['8', 'you', 'j']
print('El valor de mi variable e es:', e)
d.append(e)
print('Añado la lista de mi variable e a la lista de mi variable d y queda:', d)

#lista vacía
f=[]
print('El valor de mi variable f es una lista vacía:', f)

#diccionario
g={
  'España': 'Madrid',
  'Portugal': 'Oporto',
  'Francia': 'París'
}
print('El valor de mi variable g es un diccionario:',g, type(g))

#elementos de diccionario
print('Imprimo solo el valor de una de las claves del diccionario:', g['España'])

#alteraciones de valores de una clave de diccionarios
g['Portugal'] = 'Lisboa'
print('Le cambio el valor a una clave del diccionario', g)

#eliminaciones de claves de diccionarios
g.pop('España')
print('Elimino una de las claves del diccionario', g)

#eliminaciones de claves y recuperación de la misma en una nueva variable
h=g.pop('Francia')
print('Elimino una clave del diccionario y la almaceno en una nueva variable llamada h:', g)
print('El valor de la nueva variable h es el valor de la clave eliminada:', h)

#set
i={0, 1, 1, 1, 2, 3, 5, 6, 8, 8}
print('El valor de la variable i es un set: ', i, 'Veo que no se imprimen todos los valores que le he dado, no se imprimen los duplicados.', type(i))

#suma de sets
j={0, 2, 5, 7}
k={1, 6, 7, 0}
print('Suma de sets. No se suman los valores duplicados:', j|k)

#intersección de sets
print('Intersección de sets. Muestra los elementos que coinciden en los dos sets', j&k)

#diferencia de sets
print('Diferencia de sets. Muestra los elementos que son diferentes del primer set que no aparecen en el segundo', j-k)

#diferencia simétrica de sets
print('Diferencia simétrica de sets. Muestra los elementos que son diferentes de los dos sets', j^k)

#Métodos
p='Hola, esto es un textO'

print(p.capitalize())

print(p.title())

print(p.lower())

print(p.upper())

print(p.replace('e', 'i'))

print(p.find('es'))

print(p.split())

print(p.split(','))

print(p.replace(',', ' ').lower().split())

q = ['hola', 'esto', 'es', 'un', 'texto']

print(' '.join(q))

print(p.isnumeric())

#operadores

r=70
s=30

print(r+s)
print(r-s)
print(r*s)
print(round(r/s, 5))
print(r//s)
print(r%s)
print(r**s)

r += 5
print(r)
s -= 15
print(s)