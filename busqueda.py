# Implementación de funciones de búsqueda

def busquedalineal(lista_pokemon, nombre):
    """recorre el equipo principal  buscando un Pokemon por nombre"""
    for pokemon in lista_pokemon:
        if pokemon.nombre.lower() == nombre.lower():
            return pokemon
    return None


def busquedabinaria(ids_ordenados, pokedex, id_buscado):
    """busqueda binaria sobre la lista ordenada de ids de la pokedex"""
    izquierda = 0
    derecha = len(ids_ordenados) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        id_medio = ids_ordenados[medio]
        if id_medio == id_buscado:
            return pokedex.obtener_por_id(id_medio)
        elif id_medio < id_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return None