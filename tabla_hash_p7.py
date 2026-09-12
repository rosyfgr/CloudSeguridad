TAMANO = 10
tabla_hash = [None] * TAMANO


def funcion_hash(clave):
    return clave % TAMANO


def insertar(clave):
    posicion = funcion_hash(clave)
    posicion_inicial = posicion

    while tabla_hash[posicion] is not None:
        print("Colisión en la posición:", posicion)
        posicion = (posicion + 1) % TAMANO

        if posicion == posicion_inicial:
            print("La tabla Hash está llena.")
            return

    tabla_hash[posicion] = clave
    print("Clave", clave, "almacenada en la posición", posicion)


def mostrar_tabla():
    print("\nTABLA HASH")
    print("----------------")

    for posicion in range(TAMANO):
        print(posicion, ":", tabla_hash[posicion])


def buscar(clave):
    posicion = funcion_hash(clave)
    posicion_inicial = posicion

    while tabla_hash[posicion] is not None:

        if tabla_hash[posicion] == clave:
            print("Clave encontrada en la posición:", posicion)
            return posicion

        posicion = (posicion + 1) % TAMANO

        if posicion == posicion_inicial:
            break

    print("Clave no encontrada.")
    return None


def eliminar(clave):
    posicion = buscar(clave)

    if posicion is not None:
        tabla_hash[posicion] = None
        print("Clave", clave, "eliminada.")


datos = [27, 18, 29, 38, 13, 17, 48]

for dato in datos:
    insertar(dato)

mostrar_tabla()

print("\nELIMINACION")
print("----------------")

eliminar(13)

mostrar_tabla()