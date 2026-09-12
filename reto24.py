TAMANO = 10

tabla_hash = [None] * TAMANO

def funcion_hash(matricula):
    return matricula % TAMANO

def registrar(estudiante):
    matricula = estudiante["matricula"]
    posicion = funcion_hash(matricula)
    posicion_inicial = posicion

    while tabla_hash[posicion] is not None:
        print("Colisión en la posición:", posicion)

        posicion = (posicion + 1) % TAMANO

        if posicion == posicion_inicial:
            print("La tabla Hash está llena.")
            return

    tabla_hash[posicion] = estudiante

    print("Estudiante registrado en la posición:", posicion)

def buscar(matricula):
    posicion = funcion_hash(matricula)
    posicion_inicial = posicion

    while tabla_hash[posicion] is not None:

        if tabla_hash[posicion]["matricula"] == matricula:
            print("Estudiante encontrado en la posición:", posicion)
            print(tabla_hash[posicion])
            return posicion

        posicion = (posicion + 1) % TAMANO

        if posicion == posicion_inicial:
            break

    print("La matrícula", matricula, "no existe.")
    return None

def mostrar_tabla():
    print("\nESTUDIANTES REGISTRADOS")
    
    for posicion in range(TAMANO):
        if tabla_hash[posicion] is None:
            print(posicion, ": vacío")
        else:
            print(posicion, ":", tabla_hash[posicion])

def eliminar(matricula):
    posicion = buscar(matricula)

    if posicion is not None:
        tabla_hash[posicion] = None
        print("Estudiante con matrícula", matricula, "eliminado.")

estudiante1 = {
    "matricula": 20230121,
    "nombre": "Ana López",
    "carrera": "Sistemas Computacionales",
    "semestre": 5
}

estudiante2 = {
    "matricula": 20230131,
    "nombre": "Luis Pérez",
    "carrera": "Ingeniería Industrial",
    "semestre": 3
}

estudiante3 = {
    "matricula": 20230141,
    "nombre": "María Ruiz",
    "carrera": "Mecatrónica",
    "semestre": 7
}

estudiante4 = {
    "matricula": 23670050,
    "nombre": "Alejandra",
    "carrera": "ISC",
    "semestre": 7
}

print("REGISTRO DE ESTUDIANTES")

registrar(estudiante1)
registrar(estudiante2)
registrar(estudiante3)
registrar(estudiante4)

mostrar_tabla()

print("\nBÚSQUEDA DE ESTUDIANTES")

buscar(20230131)
buscar(99999999)
buscar(23670050)

print("\nELIMINACIÓN DE ESTUDIANTE")

eliminar(20230121)
eliminar(11111111)

mostrar_tabla()