#ordenamos por nombre, tipo y poder usando buble sort insertion sort y quick sort

def bubblesort(lista_pokemon):
    lista = lista_pokemon[:]
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j].nombre.lower() > lista[j + 1].nombre.lower():
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def insertionsort(lista_pokemon):
    lista = lista_pokemon[:]
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j].tipo.lower() > actual.tipo.lower():
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista


def quicksort(lista_pokemon):
    if len(lista_pokemon) <= 1:
        return lista_pokemon[:]
    pivote = lista_pokemon[len(lista_pokemon) // 2]
    mayores = [p for p in lista_pokemon if p.poder_combate > pivote.poder_combate]
    iguales = [p for p in lista_pokemon if p.poder_combate == pivote.poder_combate]
    menores = [p for p in lista_pokemon if p.poder_combate < pivote.poder_combate]
    return quicksort(mayores) + iguales + quicksort(menores)