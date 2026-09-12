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


insertar(27)
print(tabla_hash)