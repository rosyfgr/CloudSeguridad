TAMANO = 10
tabla_hash = [None] * TAMANO

print(tabla_hash)

def funcion_hash(clave):
    return clave % TAMANO

print(funcion_hash(27))