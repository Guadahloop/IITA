# 1) Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área del rectángulo.

# class Rectangulo():
#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura

#     def area(self):
#         return self.base * self.altura

# rectangulo1 = Rectangulo(5, 10)
# print(f"El area del rectangulo es:",rectangulo1.area())

# rectangulo2 = Rectangulo(3, 8)
# print(f"El area del rectangulo es:",rectangulo2.area())


#2) Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. La clase debe contener como miembros:
#o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
#o Un atributo para el estado (lleno o vacío).
#o Un atributo n, que indica la cantidad máxima de cebadas.
#o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
#o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
#o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso: 
# “Advertencia: el mate está lavado.” pero no se debe lanzar una excepción.

# class Mate():
#     def __init__(self, n):   
#        self.n = n   #n = cant max de cebadas
#        self.cebadas_restantes = n
#        self.lleno = False

#     def cebar(self):
#         if self.lleno:
#                print("¡Cuidado! ¡Te quemaste!")
#         else:
#             self.lleno = True

#     def beber(self):
#         if not self.lleno:
#                print("¡El mate está vacío!")
#         else:
#              self.lleno = False
#              if self.cebadas_restantes > 0:
#                   self.cebadas_restantes -= 1
#              else:
#                   print("Advertencia: el mate está lavado.")

# mate = Mate(3)

# mate.beber()  #Mate vacio
# mate.cebar()
# mate.beber()

# mate.cebar()
# mate.beber()

# mate.cebar()
# mate.beber()  #Mate lavado

# mate.cebar()
# mate.beber()  

# mate.cebar()
# mate.cebar()  #Te quemaste


#3) Botella y Sacacorchos
#  Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
#  Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está destapada.
#  Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde una referencia al corcho sacado. 
# Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el sacacorchos ya contiene un corcho.
#  Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya un corcho.

# class Corcho():
#     def __init__(self, bodega):
#         self.bodega = bodega

# class Botella():
#     def __init__(self, corcho=None):
#         self.corcho = corcho

# class Sacacorchos():
#     def __init__(self):
#         self.corcho = None

#     def destapar(self, botella):
#         if botella.corcho is None:
#             print("La botella ya esta destapada.")

#         elif self.corcho is not None:
#             print("El sacacorchos ya tiene un corcho.")

#         else:
#             self.corcho = botella.corcho
#             botella.corcho = None
#             print("Botella destapada.")

#     def limpiar(self):
#         if self.corcho is None:
#             print("No hay corcho para limpiar.")
#         else:
#             print(f"Corcho de la bodega '{self.corcho.bodega}' sacado del sacacorchos.")
#             self.corcho = None

# corcho1 = Corcho("El Porvenir")
# botella1 = Botella(corcho1)
# sacacorchos = Sacacorchos()

# sacacorchos.destapar(botella1)  #Destapa la botella
# sacacorchos.destapar(botella1)  #Botella destapada
# sacacorchos.limpiar()           #Corcho sacado
# sacacorchos.limpiar()           #No hay corcho


#4) Una heladería es un tipo especial de restaurante.
# Cree una clase Restaurante, cuyo método __init__() guarde dos atributos: restaurante_nombre y tipo_comida. 
# Cree un método describir_restaurante() que muestre estas piezas de información, y un método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. 
# Luego cree una clase Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los sabores de helado disponibles. 
# Escriba también un método que muestre estos valores, cree una instancia de la clase y llame al método.

# class Restaurante():
#     def __init__(self, restaurante_nombre, tipo_comida):
#         self.restaurante_nombre = restaurante_nombre
#         self.tipo_comida = tipo_comida
    
#     def describir_restaurante(self):
#         print(f"Restaurante: {self.restaurante_nombre}")
#         print(f"Tipo de comida: {self.tipo_comida}")

#     def abrir_restaurante(self):
#         print(f"{self.restaurante_nombre} esta abierto")

# class Heladeria(Restaurante):
#     def __init__(self, restaurante_nombre, sabores):
#         self.restaurante_nombre = restaurante_nombre
#         self.tipo_comida = "Helados"
#         self.sabores = sabores

#     def mostrar_sabores(self):
#         print(f"Sabores disponibles: {self.sabores}")

# heladeria1 = Heladeria("Fili", ["Dulce de leche", "Vainilla", "Frutilla", "Pistacho", "Chocolate"])

# heladeria1.describir_restaurante()
# heladeria1.abrir_restaurante()
# heladeria1.mostrar_sabores()


# 5) Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos recibir_ataque, que reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser menor o igual que cero, y mover que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.
#  Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que reciba otro personaje, al que le debe hacer el daño indicado por el atributo ataque.
#  Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, que devuelva la cantidad cosechada

# class Personaje():
#     def __init__(self, vida, posicion, velocidad):
#         self.vida = vida
#         self.posicion = posicion
#         self.velocidad = velocidad

#     def recibir_ataque(self, cantidad):
#         self.vida -= cantidad
#         if self.vida <= 0:
#             print("El personaje ha muerto.")
#         else:
#             print(f"Vidas restantes: {self.vida}")

#     def mover(self, direccion):
#         if direccion == "derecha":
#             self.posicion += self.velocidad
#         elif direccion == "izquierda":
#             self.posicion -= self.velocidad
#         else:
#             print("Direccion no valida.")
#         print(f"Nueva posicion: {self.posicion}")

# class Soldado(Personaje):
#     def __init__(self, vida, posicion, velocidad, ataque):
#         self.vida = vida
#         self.posicion = posicion
#         self.velocidad = velocidad
#         self.ataque = ataque

#     def atacar(self, otro_personaje):
#         print(f"Atacando con {self.ataque} de danio.")
#         otro_personaje.recibir_ataque(self.ataque)

# class Campesino(Personaje):
#     def __init__(self, vida, posicion, velocidad, cosecha):
#         self.vida = vida
#         self.posicion = posicion
#         self.velocidad = velocidad
#         self.cosecha = cosecha

#     def cosechar(self):
#         print(f"Cosechaste {self.cosecha} unidades.")
#         return self.cosecha
    

# soldado = Soldado(vida=100, posicion=0, velocidad=2, ataque=30)
# campesino = Campesino(vida=50, posicion=5, velocidad=1, cosecha=10)

# soldado.mover("derecha")
# campesino.mover("izquierda")

# campesino.cosechar()

# soldado.atacar(campesino)
# soldado.atacar(campesino)


#6) Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen de la información del usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
#Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno.

# class Usuario():
#     def __init__(self, nombre, apellido, edad, ciudad, email):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.ciudad = ciudad
#         self.email = email

#     def describir_usuario(self):
#         print("Perfil de usuario")
#         print(f"Nombre: {self.nombre} {self.apellido}")
#         print(f"Edad: {self.edad}")
#         print(f"Ciudad: {self.ciudad}")
#         print(f"Email: {self.email}")
#         print("\n")

#     def saludar_usuario(self):
#         print(f"Hola {self.nombre}!\n")

# usuario1 = Usuario("Grisel", "Perez", 28, "Rosario", "grisel@email.com")
# usuario2 = Usuario("Lucas", "Ramirez", 26, "Cordoba", "lucas@email.com")
# usuario3 = Usuario("Ana", "Lopez", 22, "Buenos Aires", "ana@email.com")

# usuario1.describir_usuario()
# usuario1.saludar_usuario()

# usuario2.describir_usuario()
# usuario2.saludar_usuario()

# usuario3.describir_usuario()
# usuario3.saludar_usuario()


#7) Admin: Un administrador es un tipo de usuario con privilegios especiales. 
# Cree una clase Admin que herede de la clase Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings tales como “puede postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc. 
# Escriba un método mostrar_privilegios() que muestre el conjunto de privilegios del administrador, cree una instancia de la clase y llame al método.

# class Usuario():
#     def __init__(self, nombre, apellido, edad, ciudad, email):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.ciudad = ciudad
#         self.email = email

#     def describir_usuario(self):
#         print("Perfil de usuario")
#         print(f"Nombre: {self.nombre} {self.apellido}")
#         print(f"Edad: {self.edad}")
#         print(f"Ciudad: {self.ciudad}")
#         print(f"Email: {self.email}")
#         print("\n")

#     def saludar_usuario(self):
#         print(f"Hola {self.nombre}!\n")

# class Admin(Usuario):
#     def __init__(self, nombre, apellido, edad, ciudad, email):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.ciudad = ciudad
#         self.email = email
#         self.privilegios = [
#             "1. Puede postear en el foro.",
#             "2. Puede borrar un post.",
#             "3. Puede banear usuarios."
#         ]

#     def mostrar_privilegios(self):
#         print("Privilegios del administrador:\n")
#         for privilegio in self.privilegios:
#             print(f"{privilegio}")

# admin1 = Admin("Marcela", "Gomez", 40, "Mendoza", "maria.admin@email.com")

# admin1.describir_usuario()
# admin1.saludar_usuario()
# admin1.mostrar_privilegios()


#8) Privilegios: Escriba una clase Privilegios. La clase debería tener un atributo, privilegios, que almacene una lista de strings con los privilegios de manera similar a la del ejercicio 7. 
# Mueva el método mostrar_privilegios() de ese ejercicio a esta clase, y haga que una instancia de esta clase sea un atributo de la clase Admin. 
# Cree una nueva instancia de Admin y use el método para mostrar privilegios.


#Privilegios

# class Privilegios():
#     def __init__(self):
#         self.privilegios = [
#             "1. Puede postear en el foro.",
#             "2. Puede borrar un post.",
#             "3. Puede banear usuarios."
#         ]
#     def mostrar_privilegios(self):
#         print("Privilegios del administrador:\n")
#         for privilegio in self.privilegios:
#             print(f"{privilegio}")

# #Usuario

# class Usuario():
#     def __init__(self, nombre, apellido, edad, ciudad, email):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.ciudad = ciudad
#         self.email = email

#     def describir_usuario(self):
#         print("Perfil de usuario")
#         print(f"Nombre: {self.nombre} {self.apellido}")
#         print(f"Edad: {self.edad}")
#         print(f"Ciudad: {self.ciudad}")
#         print(f"Email: {self.email}")
#         print("\n")

#     def saludar_usuario(self):
#         print(f"Hola {self.nombre}!\n")
        
# #Admin y Privilegios

# class Admin(Usuario):
#     def __init__(self, nombre, apellido, edad, ciudad, email):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.ciudad = ciudad
#         self.email = email
#         self.privilegios = Privilegios()


# admin2 = Admin("Lucas", "Fernandez", 35, "Rosario", "lucas.admin@email.com")

# admin2.describir_usuario()
# admin2.saludar_usuario()
# admin2.privilegios.mostrar_privilegios()


#9) Restaurante importado: Escriba un programa que esté en otro archivo que la clase Restaurante del ejercicio 4, e impórtela al módulo actual. 
# Cree una instancia de Restaurante y llame a alguno de sus métodos para asegurarse que la importación funcionó.

# from restaurante import Restaurante

# restaurante1 = Restaurante("Nino Helados", "Heladeria artesanal")
# restaurante1.describir_restaurante()
# restaurante1.abrir_restaurante()

#10) (Opcional): Repita el ejercicio anterior pero esta vez importando la clase Heladeria. 
# ¿Qué se necesita para que funcione la importación?

# from restaurante import Restaurante
# from heladeria import Heladeria

# class Heladeria(Restaurante):
#     def __init__(self, restaurante_nombre, sabores):
#         self.restaurante_nombre = restaurante_nombre
#         self.tipo_comida = "Helados"
#         self.sabores = sabores

#     def mostrar_sabores(self):
#         print(f"Sabores disponibles: {self.sabores}")

# heladeria1 = Heladeria("Fili", ["Dulce de leche", "Vainilla", "Frutilla", "Pistacho", "Chocolate"])

# heladeria1.describir_restaurante()
# heladeria1.abrir_restaurante()
# heladeria1.mostrar_sabores()
