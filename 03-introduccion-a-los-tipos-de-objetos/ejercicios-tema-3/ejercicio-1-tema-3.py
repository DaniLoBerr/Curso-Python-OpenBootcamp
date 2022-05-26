'''
Para este ejercicio tenéis que crear en la consola de python variables que representen los siguientes datos de un contacto:

Nombre
Apellidos
Edad
Email
Teléfono
Casado (verdadero o falso)
Con Hijos (verdadero o falso)
Lista de amigos
Películas vistas (diccionario con clave y valor. El valor será el título de la película)

Una vez hayas creado todas las variables, muéstralas por consola haciendo uso de la función print().

Tienes que subir capturas de pantalla en una carpeta comprimida zip.
'''

nombre = 'Daniel'
print('Nombre:', nombre)
apellidos = ('López', 'Berrocal')
print('Apellidos:', apellidos)
edad = 29
print('Edad:', edad, 'años')
email = 'miemail@email.com'
print('E-mail:', email)
telefono = 666666666
print('Teléfono:', telefono)
casado = False
print('Casado:', casado)
hijos = False
print('Con hijos:', hijos)
amigos = ['David', 'María', 'Mateo', 'Gonzalo', 'Carolina']
print('Lista de amigos:', amigos)
peliculasVistas =  {
  'pelicula1': 'Pulp Fiction',
  'pelicula2': 'Reservoir Dogs',
  'pelicula3': 'Django'
}
print('Películas vistas:', peliculasVistas)