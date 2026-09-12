TAMANO = 10

matriculas = [
    20230121,
    20230135,
    20230147,
    20230155,
    20230168,
    20230175,
    20230185
]


def probar_funcion_hash(nombre, funcion_hash):
    tabla_hash = [None] * TAMANO
    colisiones = 0

    print("\n", nombre)
    print("----------------------------")

    for matricula in matriculas:
        posicion = funcion_hash(matricula)
        posicion_inicial = posicion

        while tabla_hash[posicion] is not None:
            colisiones += 1
            print(
                "Colisión con matrícula",
                matricula,
                "en posición",
                posicion
            )

            posicion = (posicion + 1) % TAMANO

            if posicion == posicion_inicial:
                print("La tabla Hash está llena.")
                break

        tabla_hash[posicion] = matricula

    print("\nTABLA RESULTANTE")

    for posicion in range(TAMANO):
        print(posicion, ":", tabla_hash[posicion])

    print("Colisiones producidas:", colisiones)

    return colisiones


def funcion_a(clave):
    return clave % TAMANO


def funcion_b(clave):
    return (clave * 3) % TAMANO


def funcion_c(clave):
    return (clave * 7 + 3) % TAMANO


print("COMPARACIÓN DE FUNCIONES HASH")
print("==============================")


colisiones_a = probar_funcion_hash(
    "FUNCIÓN A: k % m",
    funcion_a
)

colisiones_b = probar_funcion_hash(
    "FUNCIÓN B: (k * 3) % m",
    funcion_b
)

colisiones_c = probar_funcion_hash(
    "FUNCIÓN C: (k * 7 + 3) % m",
    funcion_c
)


print("\nRESUMEN")
print("")
print("Función Hash\t\tColisiones")
print("k % m\t\t\t", colisiones_a)
print("(k * 3) % m\t\t", colisiones_b)
print("(k * 7 + 3) % m\t", colisiones_c)


menor = min(
    colisiones_a,
    colisiones_b,
    colisiones_c
)

print("\nFUNCIÓN CON MENOS COLISIONES")

if menor == colisiones_a:
    print("k % m")

elif menor == colisiones_b:
    print("(k * 3) % m")

else:
    print("(k * 7 + 3) % m")