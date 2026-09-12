matriculas = [
    20230121,
    20230135,
    20230147,
    20230155,
    20230168,
    20230175,
    20230185
]


def ejecutar_experimento(tamano):
    tabla_hash = [None] * tamano
    colisiones = 0

    def funcion_hash(clave):
        return clave % tamano

    def insertar(clave):
        nonlocal colisiones

        posicion = funcion_hash(clave)
        posicion_inicial = posicion

        while tabla_hash[posicion] is not None:
            colisiones += 1
            posicion = (posicion + 1) % tamano

            if posicion == posicion_inicial:
                print("La tabla Hash está llena.")
                return

        tabla_hash[posicion] = clave

    for matricula in matriculas:
        insertar(matricula)

    print("\nTAMAÑO DE TABLA:", tamano)
    print("----------------------------")

    for posicion in range(tamano):
        print(posicion, ":", tabla_hash[posicion])

    print("Número de claves:", len(matriculas))
    print("Número de colisiones:", colisiones)

    return colisiones


print("EXPERIMENTOS DE TAMAÑO DE TABLA")
print("================================")

colisiones_10 = ejecutar_experimento(10)
colisiones_15 = ejecutar_experimento(15)
colisiones_20 = ejecutar_experimento(20)


print("\nRESUMEN")
print("--------------------------------")
print("Tamaño\tClaves\tColisiones")
print("10\t7\t", colisiones_10)
print("15\t7\t", colisiones_15)
print("20\t7\t", colisiones_20)