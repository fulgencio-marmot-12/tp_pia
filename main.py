import random

from clases import Pokemon, Pokedex
from ordenamiento import bubblesort, insertionsort, quicksort
from entrenador import Entrenador
from busqueda import busquedabinaria, busquedalineal

RUTA_POKEMONES = "data/pokemones.json"
RUTA_MEDALLAS = "data/medallas.json"

GIMNASIOS = [
    "Medalla Roca", "Medalla Cascada", "Medalla Trueno", "Medalla Arcoíris",
    "Medalla Alma", "Medalla Pantano", "Medalla Volcán", "Medalla Tierra",
]

POOL_POKEMON_SALVAJES = [
    ("Caterpie", "Bicho"), ("Weedle", "Bicho"), ("Spearow", "Volador"),
    ("Ekans", "Veneno"), ("Sandshrew", "Tierra"), ("Vulpix", "Fuego"),
    ("Growlithe", "Fuego"), ("Poliwag", "Agua"), ("Abra", "Psíquico"),
    ("Magnemite", "Eléctrico"),
]

contador_ids_salvajes = 9000


def mostrar_pokedex(pokedex):
    print("  POKEDEX NACIONAL ")
    for pokemon in sorted(pokedex.obtener_todos(), key=lambda p: p.id):
        print(pokemon)


def mostrar_equipo(entrenador):
    print("\n EQUIPO PRINCIPAL ")
    if not entrenador.equipo_principal:
        print("el equipo está vacio")
    for pokemon in entrenador.equipo_principal:
        print(pokemon)


def mostrar_pc(entrenador):
    print("\n ALMACENAMIENTO PC ")
    pokemones_pc = entrenador.pc.a_lista_python()
    if not pokemones_pc:
        print("La PC está vacía.")
    for pokemon in pokemones_pc:
        print(pokemon)


def capturar_pokemon(entrenador):
    global contador_ids_salvajes
    nombre, tipo = random.choice(POOL_POKEMON_SALVAJES)
    poder_combate = random.randint(150, 2800)
    contador_ids_salvajes += 1
    nuevo_pokemon = Pokemon(contador_ids_salvajes, nombre, tipo, poder_combate)
    print(f"\nSISTEMA DE CAPTURA aparecio un {nombre.upper()} salvaje (PC: {poder_combate}).")
    print("Captura exitosa")
    entrenador.capturar_pokemon(nuevo_pokemon)


def ordenar_pc(entrenador):
    pokemones_pc = entrenador.pc.a_lista_python()
    if not pokemones_pc:
        print("La PC está vacía, no hay nada para ordenar")
        return
    print("\n--- ORDENAR PC ---")
    print("1. Alfabético por bubble sort")
    print("2. Por tipo por insertion sort")
    print("3. Por poder de combate por quick sort")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        ordenados = bubblesort(pokemones_pc)
    elif opcion == "2":
        ordenados = insertionsort(pokemones_pc)
    elif opcion == "3":
        ordenados = quicksort(pokemones_pc)
    else:
        print("opción inválida")
        return
    entrenador.pc.cargar_desde_lista(ordenados)
    print("PC ordenada exitosamente:")
    for pokemon in ordenados:
        print(pokemon)


def buscar_en_equipo(entrenador):
    nombre = input("nombre del Pokémon a buscar en el equipo: ")
    encontrado = busquedalineal(entrenador.equipo_principal, nombre)
    if encontrado:
        print(f"encontrado {encontrado}")
    else:
        print(f"{nombre} no se encuentra en el equipo orincipal")


def consultar_pokedex_por_id(pokedex):
    try:
        id_buscado = int(input("Ingrese el ID a buscar en la Pokédex: "))
    except ValueError:
        print("Debe ingresar un número entero")
        return
    ids_ordenados = pokedex.obtener_ids_ordenados()
    resultado = busquedabinaria(ids_ordenados, pokedex, id_buscado)
    if resultado:
        print(f"pokemon encontrado: {resultado}")
    else:
        print(f"no existe ningún Pokémon con ID {id_buscado} en la Pokédex")


def transferir_a_oak(entrenador):
    nombre = input("Nombre del Pokémon a transferir desde la PC: ")
    entrenador.transferir_a_oak(nombre)


def desafiar_gimnasio(entrenador):
    print("\n--- GIMNASIOS DISPONIBLES ---")
    for indice, medalla in enumerate(GIMNASIOS, start=1):
        print(f"{indice}. {medalla.replace('Medalla ', '')}")
    try:
        opcion = int(input("Elija un gimnasio (1-8): "))
    except ValueError:
        print("Opción inválida.")
        return
    if opcion < 1 or opcion > len(GIMNASIOS):
        print("Opción inválida.")
        return
    medalla = GIMNASIOS[opcion - 1]
    print(f"\nDesafiando al Líder del gimnasio de {medalla.replace('Medalla ', '')}...")
    gano = random.choice([True, False])
    if gano:
        print("¡Has ganado la batalla!")
        entrenador.medallas.agregar_medalla(medalla)
    else:
        print("Has perdido la batalla. El líder te espera para la revancha.")


def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Ver Pokédex")
    print("2. Ver Equipo Principal")
    print("3. Ver PC")
    print("4. Capturar nuevo Pokémon")
    print("5. Ordenar PC")
    print("6. Buscar Pokémon en Equipo")
    print("7. Consultar Pokémon por ID en Pokédex")
    print("8. Enviar Pokémon al Centro Pokémon")
    print("9. Transferir Pokémon al Profesor Oak")
    print("10. Deshacer última transferencia")
    print("11. Desafiar Líder de Gimnasio")
    print("12. Salir del sistema")


def main():
    print("SISTEMA DE GESTIÓN: POKÉMON HUERGO")
    print("Inicializando motor de base de datos")
    pokedex = Pokedex(RUTA_POKEMONES)
    print(f"Cargando Pokédex Nacional ({len(pokedex.obtener_todos())} registros)")
    entrenador = Entrenador(RUTA_MEDALLAS)
    print("Validando registros de medallas")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_pokedex(pokedex)
        elif opcion == "2":
            mostrar_equipo(entrenador)
        elif opcion == "3":
            mostrar_pc(entrenador)
        elif opcion == "4":
            capturar_pokemon(entrenador)
        elif opcion == "5":
            ordenar_pc(entrenador)
        elif opcion == "6":
            buscar_en_equipo(entrenador)
        elif opcion == "7":
            consultar_pokedex_por_id(pokedex)
        elif opcion == "8":
            entrenador.enviar_a_centro_pokemon()
        elif opcion == "9":
            transferir_a_oak(entrenador)
        elif opcion == "10":
            entrenador.deshacer_transferencia()
        elif opcion == "11":
            desafiar_gimnasio(entrenador)
        elif opcion == "12":
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        else:
            print("Opción inválida, intente nuevamente.")


if __name__ == "__main__":
    main()