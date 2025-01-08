from Class_Fecha import Fecha
from Class_Direccion import Direccion
from Class_Usuario import Usuario
from NodListSimple import ListaSimple
from NodListDoble import ListaDoble

# Crear una lista de usuarios predefinidos
lista_usuarios = ListaDoble()

# Crear y agregar usuarios predefinidos a la lista
fecha_nacimiento1 = Fecha(8, 5, 1996)
direccion_residencia1 = Direccion("Carrera_72B", "96-76", "Castilla", "Medellin", "Edificio_1", "201")
usuario1 = Usuario("Juan-Herrera", 1066751353)
usuario1.setFecha_nacimiento(fecha_nacimiento1)
usuario1.setCiudad_nacimiento("Planeta_Rica")
usuario1.setTel(3206078405)
usuario1.setEmail("jherrerasi@unal.edu.co")
usuario1.setDir(direccion_residencia1)
lista_usuarios.addLast(usuario1)

fecha_nacimiento2 = Fecha(3, 6, 2000)
direccion_residencia2 = Direccion("Calle_68A", "97-12", "Manrrique", "Medellin", "Edificio_3", "204")
usuario2 = Usuario("Carlos-Lozano", 1062375428)
usuario2.setFecha_nacimiento(fecha_nacimiento2)
usuario2.setCiudad_nacimiento("Pereira")
usuario2.setTel(3235242873)
usuario2.setEmail("jglozanoju@unal.edu.co")
usuario2.setDir(direccion_residencia2)
lista_usuarios.addLast(usuario2)

fecha_nacimiento3 = Fecha(5, 9, 2005)
direccion_residencia3 = Direccion("Calle_65", "12-23", "Estadio", "Medellin", "Edificio_5", "305")
usuario3 = Usuario("Vicente-Fernandez", 75272635)
usuario3.setFecha_nacimiento(fecha_nacimiento3)
usuario3.setCiudad_nacimiento("Manizales")
usuario3.setTel(324274653)
usuario3.setEmail("hgfernandezte@unal.edu.co")
usuario3.setDir(direccion_residencia3)
lista_usuarios.addLast(usuario3)

fecha_nacimiento4 = Fecha(26, 2, 2003)
direccion_residencia4 = Direccion("Calle_28", "15-23", "Lureles", "Medellin", "Edificio_1", "505")
usuario4 = Usuario("Victor-Sibaja", 1064254526)
usuario4.setFecha_nacimiento(fecha_nacimiento4)
usuario4.setCiudad_nacimiento("Monteria")
usuario4.setTel(3113567253)
usuario4.setEmail("vsibajach@unal.edu.co")
usuario4.setDir(direccion_residencia4)
lista_usuarios.addLast(usuario4)

fecha_nacimiento5 = Fecha(31, 12, 2008)
direccion_residencia5 = Direccion("Calle_33", "35-22", "Paris", "Medellin", "Edificio_2", "101")
usuario5 = Usuario("Yadira-Chavez", 1063284523)
usuario5.setFecha_nacimiento(fecha_nacimiento5)
usuario5.setCiudad_nacimiento("Montelibano")
usuario5.setTel(3152432675)
usuario5.setEmail("ychavezfg@unal.edu.co")
usuario5.setDir(direccion_residencia5)
lista_usuarios.addLast(usuario5)

# Imprimir los usuarios predefinidos
print("Usuarios Predefinidos:")
current = lista_usuarios.head
while current:
    print(current.data.toString())  # Imprime los datos de cada usuario
    current = current.next

# Insertar un nuevo usuario al principio
print("\nInsertando usuario al principio:")
nombre = input("Ingrese el nombre del nuevo usuario: ")
id_usuario = int(input("Ingrese el ID del nuevo usuario: "))
nuevo_usuario = Usuario(nombre, id_usuario)
lista_usuarios.addFirst(nuevo_usuario)  # Insertar al principio

# Mostrar lista después de insertar al principio
current = lista_usuarios.head
while current:
    print(current.data.toString())  # Imprimir la lista actualizada
    current = current.next

# Insertar un nuevo usuario al final
print("\nInsertando usuario al final:")
nombre = input("Ingrese el nombre del nuevo usuario: ")
id_usuario = int(input("Ingrese el ID del nuevo usuario: "))
nuevo_usuario = Usuario(nombre, id_usuario)
lista_usuarios.addFirst(nuevo_usuario)  # Insertar al principio
# Mostrar lista después de insertar al final
current = lista_usuarios.head
while current:
    print(current.data.toString())  # Imprimir la lista actualizada
    current = current.next

# Insertar un usuario después del tercer nodo
print("\nInse rtando usuario después del tercer nodo:")
nombre = input("Ingrese el nombre del nuevo usuario: ")
id_usuario = int(input("Ingrese el ID del nuevo usuario: "))
nuevo_usuario = Usuario(nombre, id_usuario)
lista_usuarios.addLast(nuevo_usuario)  # Insertar al principio 

# Mostrar lista después de la inserción en la posición específica
current = lista_usuarios.head
while current:
    print(current.data.toString())  # Imprimir la lista actualizada
    current = current.next