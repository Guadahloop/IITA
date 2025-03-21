#1) Hacer un programa que gestiones datos para una escuela.
# El programa tiene que ser capaz de:
# a) Llevar un registro de todos los datos de alumnos de la escuela (Nombre, Apellido, fecha de nacimiento, DNI, Nombre de Tutor, registro de todas las notas, cantidad de faltas, cantidad de amonestaciones recibidas.
# Recomendación: Para llevar un registro de estos dato se puede utilizar un diccionario estructurado de la siguiente manera:
# {
# “Alumnos” : [alumno1,alumno2,alumno3 ]
# }
# Donde cada alumno es otro diccionario estructurado de la
# siguiente forma:
# {
# “Nombre”: nombre de alumno,
# “Apellido” : apellido de alumno,
# “DNI” : DNI de alumno
# “Fecha de nacimiento”, fecha de nacimiento de alumno,
# “Tutor” : nombre y apellido de tutor,
# “Notas” : todas las notas del alumno,
# “Faltas” : cantidad de faltas,
# “amonestaciones” : cantidad de amonestaciones
# }
# En esta estructura:
# Datos = {
# “Alumnos” : [alumno1,alumno2,alumno3 ]
# }
# Para acceder por ejemplo al numero de DNI del tercer alumno podríamos hacer algo así:
# Datos[“Alumnos”][2][“DNI”]
# Este es un ejemplo de estructura, se puede cambiar completamente o hacer algunos cambios sobre el para mejorar el orden (si lo consideran necesario)
# b) Mostrar los datos de cada alumno
# c) Modificar los datos de los alumnos
# d) Agregar alumnos
# e) Expulsar alumnos






import random

datos = {"Alumnos": [
    {"Nombre": "Julian", "Apellido": "Perez", "DNI": "12345678", "Fecha de nacimiento": "01/01/2012", "Tutor": "Carlos Perez", "Notas": [], "Faltas": 0, "Amonestaciones": 0},
    {"Nombre": "Maria", "Apellido": "Ibarra", "DNI": "87654321", "Fecha de nacimiento": "15/05/2012", "Tutor": "Ana Ibarra", "Notas": [], "Faltas": 0, "Amonestaciones": 0},
    {"Nombre": "Pablo", "Apellido": "Ramirez", "DNI": "11223344", "Fecha de nacimiento": "20/09/2011", "Tutor": "Jose Ramirez", "Notas": [], "Faltas": 0, "Amonestaciones": 0}
]}

def agregar_alumno():
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    dni = input("Ingrese el DNI del alumno: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno (DD/MM/AAAA): ")
    tutor = input("Ingrese el nombre del tutor del alumno: ")

    notas = [random.choice(range(1, 11)) for i in range(3)]
    faltas = random.choice(range(0, 26))
    amonestaciones = random.choice(range(0, 26))

    alumno = {
        "Nombre": nombre,
        "Apellido": apellido,
        "DNI": dni,
        "Fecha de nacimiento": fecha_nacimiento,
        "Tutor": tutor,
        "Notas": notas,
        "Faltas": faltas,
        "Amonestaciones": amonestaciones
    }
    datos["Alumnos"].append(alumno)
    print(f"Alumno {nombre} {apellido} agregado correctamente.")

def mostrar_detalle_alumno():
    dni = input("Ingrese el DNI del alumno: ")
    for alumno in datos["Alumnos"]:
        if alumno["DNI"] == dni:
          
            print(f"Nombre: {alumno['Nombre']} {alumno['Apellido']}")
            print(f"DNI: {alumno['DNI']}")
            print(f"Fecha de nacimiento: {alumno['Fecha de nacimiento']}")
            print(f"Tutor: {alumno['Tutor']}")

            notas_random = [random.choice(range(1, 11)) for i in range(3)]
            faltas_random = random.choice(range(0, 26))
            amonestaciones_random = random.choice(range(0, 26))
            print(f"Notas: {notas_random}")
            print(f"Faltas: {faltas_random}")
            print(f"Amonestaciones: {amonestaciones_random}")
            return
        
    print("Alumno no encontrado.")

def modificar_alumno():
    dni = input("Ingrese el DNI del alumno a modificar: ")
    modificaciones = {}
    
    while True:
        campo = input("Ingrese el campo a modificar (o 'salir' para terminar): ")
        if campo == 'salir':
            break
        
        if campo in ["Nombre", "Apellido", "Fecha de nacimiento", "Tutor"]:
            nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")
            modificaciones[campo] = nuevo_valor
        
        elif campo == "Notas":
            notas = []
            for i in range(3):
                nota = int(input(f"Ingrese la nota {i+1}: "))
                notas.append(nota)
            modificaciones["Notas"] = notas
        
        else:
            print("Campo invalido.")
    
    for alumno in datos["Alumnos"]:
        if alumno["DNI"] == dni:
            for campo, nuevo_valor in modificaciones.items():
                alumno[campo] = nuevo_valor
            
            print("Datos actualizados correctamente.")
            return
    
    print("Alumno no encontrado.")

def mostrar_alumnos():
    if not datos["Alumnos"]:
        print("No hay alumnos registrados.")
        return
    i = 1
    for alumno in datos["Alumnos"]:
        print(f"{i}. {alumno['Nombre']} {alumno['Apellido']} - DNI: {alumno['DNI']}")
        i += 1

def expulsar_alumno():
    dni = input("Ingrese el DNI del alumno a expulsar: ")
    for alumno in datos["Alumnos"]:
        
        if alumno["DNI"] == dni:
            datos["Alumnos"].remove(alumno)
            print("Alumno expulsado correctamente.")
            return
    
    print("Alumno no encontrado.")

def menu():
    while True:
        print("\nMenu")
        print("1. Agregar alumno")
        print("2. Mostrar alumnos")
        print("3. Mostrar detalle de un alumno")
        print("4. Modificar datos de un alumno")
        print("5. Expulsar alumno")
        print("6. Salir")
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            agregar_alumno()
        elif opcion == "2":
            mostrar_alumnos()
        elif opcion == "3":
            mostrar_detalle_alumno()
        elif opcion == "4":
            modificar_alumno()
        elif opcion == "5":
            expulsar_alumno()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida. Intente nuevamente.")

menu()