TAMANO = 10
tabla_hash = [None] * TAMANO


def funcion_hash(matricula):
    return matricula % TAMANO


def insertar(matricula):
    posicion = funcion_hash(matricula)
    posicion_inicial = posicion
    hubo_colision = False

    while tabla_hash[posicion] is not None:
        hubo_colision = True
        print("Colisión en la posición:", posicion)

        posicion = (posicion + 1) % TAMANO

        if posicion == posicion_inicial:
            print("La tabla Hash está llena.")
            return None, hubo_colision

    tabla_hash[posicion] = matricula

    print(
        "Matrícula",
        matricula,
        "almacenada en la posición",
        posicion
    )

    return posicion, hubo_colision


def mostrar_tabla():
    print("\nTABLA HASH")
    print("----------------")

    for posicion in range(TAMANO):
        print(posicion, ":", tabla_hash[posicion])


matriculas = [
    20230121,
    20230135,
    20230147,
    20230155,
    20230168,
    20230175,
    20230185
]

resultados = []

for matricula in matriculas:
    hash_inicial = funcion_hash(matricula)

    posicion_final, hubo_colision = insertar(matricula)

    resultados.append(
        (
            matricula,
            hash_inicial,
            posicion_final,
            hubo_colision
        )
    )


mostrar_tabla()


print("\nRESULTADOS")
print("-----------------------------------------------------------")
print("Matrícula\tHash inicial\tPosición final\tColisión")

for resultado in resultados:
    matricula, hash_inicial, posicion_final, hubo_colision = resultado

    if hubo_colision:
        colision = "Sí"
    else:
        colision = "No"

    print(
        matricula,
        "\t",
        hash_inicial,
        "\t\t",
        posicion_final,
        "\t\t",
        colision
    )