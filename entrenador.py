from clases import ListaEnlazada, RegistroMedallas
from stack import stack
from queue import Queue


TAMAÑO_MAXIMO_EQUIPO = 6
TAMAÑO_MAXIMO_TRANSFERENCIAS = 5


class entrenador:
    """clase con todas  las estructuras del entrenador"""

    def __init__(self, archivo_medallas=None):
        self.equipo_principal = []  # Array de maximo 6
        self.pc = ListaEnlazada()
        self.centro_pokemon = Queue()
        self.transferencias = stack(capacidad_maxima=TAMAÑO_MAXIMO_TRANSFERENCIAS)
        self.medallas = RegistroMedallas(archivo_medallas)

    def capturar_pokemon(self, pokemon):
        if len(self.equipo_principal) < TAMAÑO_MAXIMO_EQUIPO:
            self.equipo_principal.append(pokemon)
            print(f"{pokemon.nombre} se unió al equipo principal "
                  f"({len(self.equipo_principal)}/{TAMAÑO_MAXIMO_EQUIPO})")
        else:
            print("el Equipo Principal está lleno ")
            self.pc.insertar_al_inicio(pokemon)
            print(f"derivando a almacenamiento de PC {pokemon.nombre} se pudio añadir.")

    def enviar_a_centro_pokemon(self):
        if not self.equipo_principal:
            print("no hay pokemon para sanar")
            return
        for pokemon in self.equipo_principal:
            self.centro_pokemon.encolar(pokemon)
        print('enfermera Joy "estamos curando a tus pokemon"')
        while not self.centro_pokemon.esta_vacia():
            pokemon = self.centro_pokemon.desencolar()
            print(f"procesando: [{pokemon.nombre}] se esta sanado.")
        print('enfermera Joy: "tus Pokemones están en perfecta forma"')

    def buscar_pokemon_en_pc(self, nombre):
        for pokemon in self.pc.a_lista_python():
            if pokemon.nombre.lower() == nombre.lower():
                return pokemon
        return None

    def transferir_a_oak(self, nombre_pokemon):
        pokemon = self.buscar_pokemon_en_pc(nombre_pokemon)
        if pokemon is None:
            print("ese Pokémon no se encuentra en la PC")
            return
        self.pc.eliminar(pokemon)
        self.transferencias.apilar(pokemon)
        print(f"transferiste a '{pokemon.nombre}' al profesor Oak")

    def deshacer_transferencia(self):
        pokemon = self.transferencias.desapilar()
        if pokemon is None:
            print("no hay transferencias para deshacer")
            return
        self.pc.insertar_al_inicio(pokemon)
        print(f"'{pokemon.nombre}' ha vuelto a la PC")
