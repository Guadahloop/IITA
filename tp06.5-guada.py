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
# f) Dar Persistencia a los Datos del programa mediante la implementación Archivos


def guardar_alumnos():
    with open("Alumnos.txt", "w") as file:
        for alumno in datos["Alumnos"]:
            file.write(f"Nombre: {alumno['Nombre']}\n")
            file.write(f"Apellido: {alumno['Apellido']}\n")
            file.write(f"DNI: {alumno['DNI']}\n")
            file.write(f"Fecha de nacimiento: {alumno['Fecha de nacimiento']}\n")
            file.write(f"Tutor: {alumno['Tutor']}\n")
            
            notas_str = ", ".join(str(nota) for nota in alumno["Notas"])
            file.write(f"Notas: {notas_str}\n")
            
            file.write(f"Faltas: {alumno['Faltas']}\n")
            file.write(f"Amonestaciones: {alumno['Amonestaciones']}\n")
            file.write("\n")

def lista_alumnos():
    datos = {"Alumnos": []}
    with open("Alumnos.txt", "r") as file:
        alumno = {}
        for linea in file:
            linea = linea.replace("\n", "")

            if linea == "":
                if alumno:
                    datos["Alumnos"].append(alumno)
                    alumno = {}
            else:
                separador = linea.find(": ")
                if separador != -1:
                    clave = linea[:separador]
                    valor = linea[separador + 2:]
                    
                    if clave == "Notas" or clave == "Faltas" or clave == "Amonestaciones":
                        valores_numericos = []
                        acumulador = ""

                        for caracter in valor:
                            if caracter in "0123456789":
                                acumulador += caracter
                            elif caracter == ",":
                                if acumulador:
                                    valores_numericos.append(int(acumulador))
                                    acumulador = ""
                        
                        if acumulador:
                            valores_numericos.append(int(acumulador))

                        if clave == "Notas":
                            alumno[clave] = valores_numericos
                        else:
                            alumno[clave] = valores_numericos[0] if valores_numericos else 0
                    else:
                        alumno[clave] = valor

        if alumno:
            datos["Alumnos"].append(alumno)

    return datos

datos = lista_alumnos()

def agregar_alumno():
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    dni = input("Ingrese el DNI del alumno: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno (DD/MM/AAAA): ")
    tutor = input("Ingrese el nombre del tutor del alumno: ")

    notas = []
    faltas = 0
    amonestaciones = 0

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
    guardar_alumnos()


def mostrar_detalle_alumno():
    dni = input("Ingrese el DNI del alumno: ")
    for alumno in datos["Alumnos"]:
        if alumno["DNI"] == dni:
            print(f"Nombre: {alumno['Nombre']} {alumno['Apellido']}")
            print(f"DNI: {alumno['DNI']}")
            print(f"Fecha de nacimiento: {alumno['Fecha de nacimiento']}")
            print(f"Tutor: {alumno['Tutor']}")
            print(f"Notas: {alumno['Notas']}")
            print(f"Faltas: {alumno['Faltas']}")
            print(f"Amonestaciones: {alumno['Amonestaciones']}")
            return
    print("Alumno no encontrado.")


def modificar_alumno():
    dni = input("Ingrese el DNI del alumno a modificar: ")
    modificaciones = {}

    while True:
        campo = input("Ingrese el campo a modificar (o 'salir' para terminar): ")
        if campo.lower() == 'salir':
            break

        if campo in ["Nombre", "Apellido", "Fecha de nacimiento", "Tutor"]:
            modificaciones[campo] = input(f"Ingrese el nuevo valor para {campo}: ")
        elif campo == "Notas":
            notas = []
            for i in range(3):
                notas.append(int(input(f"Ingrese la nota {i + 1}: ")))
            modificaciones["Notas"] = notas
        elif campo == "Faltas" or campo == "Amonestaciones":
            modificaciones[campo] = int(input(f"Ingrese el nuevo valor para {campo}: "))
        else:
            print("Campo inválido.")

    for alumno in datos["Alumnos"]:
        if alumno["DNI"] == dni:
            for campo, nuevo_valor in modificaciones.items():
                alumno[campo] = nuevo_valor
            print("Datos actualizados correctamente.")
            guardar_alumnos()
            return

    print("Alumno no encontrado.")


def mostrar_alumnos():
    if not datos["Alumnos"]:
        print("No hay alumnos registrados.")
        return
    for i, alumno in enumerate(datos["Alumnos"], 1):
        print(f"{i}. {alumno['Nombre']} {alumno['Apellido']} - DNI: {alumno['DNI']}")


def expulsar_alumno():
    dni = input("Ingrese el DNI del alumno a expulsar: ")
    for alumno in datos["Alumnos"]:
        if alumno["DNI"] == dni:
            datos["Alumnos"].remove(alumno)
            print("Alumno expulsado correctamente.")
            guardar_alumnos()
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