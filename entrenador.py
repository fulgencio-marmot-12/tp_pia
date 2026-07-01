from listaenlazada import ListaEnlazada
from stack import stack
from queue import Queue
from clases import RegistroMedallas

TAMANIO_MAXIMO_EQUIPO = 6
TAMANIO_MAXIMO_TRANSFERENCIAS = 5


class Entrenador:
    def __init__(self, archivo_medallas=None):
        self.equipo_principal = []  # Array (lista) con tope de 6
        self.pc = ListaEnlazada()
        self.centro_pokemon = Queue()
        self.transferencias = stack(capacidad_maxima=TAMANIO_MAXIMO_TRANSFERENCIAS)
        self.medallas = RegistroMedallas(archivo_medallas)

    def capturar_pokemon(self, pokemon):
        if len(self.equipo_principal) < TAMANIO_MAXIMO_EQUIPO:
            self.equipo_principal.append(pokemon)
            print(f"{pokemon.nombre} se unió al Equipo Principal "
                  f"({len(self.equipo_principal)}/{TAMANIO_MAXIMO_EQUIPO}).")
        else:
            print("Analizando espacios... El Equipo Principal está lleno (6/6).")
            self.pc.insertar_al_inicio(pokemon)
            print(f"Derivando a Almacenamiento de PC... {pokemon.nombre} añadido exitosamente.")

    def enviar_a_centro_pokemon(self):
        if not self.equipo_principal:
            print("No tenés Pokémon en el equipo para sanar.")
            return
        for pokemon in self.equipo_principal:
            self.centro_pokemon.encolar(pokemon)
        print('Enfermera Joy: "estamos curando a tus pokémon"')
        while not self.centro_pokemon.esta_vacia():
            pokemon = self.centro_pokemon.desencolar()
            print(f"Procesando: [{pokemon.nombre}] -> Sanado.")
        print('Enfermera Joy: "¡Tus Pokémon están en perfecta forma!"')

    def buscar_pokemon_en_pc(self, nombre):
        for pokemon in self.pc.a_lista_python():
            if pokemon.nombre.lower() == nombre.lower():
                return pokemon
        return None

    def transferir_a_oak(self, nombre_pokemon):
        pokemon = self.buscar_pokemon_en_pc(nombre_pokemon)
        if pokemon is None:
            print("Ese Pokémon no se encuentra en la PC.")
            return
        self.pc.eliminar(pokemon)
        self.transferencias.apilar(pokemon)
        print(f"Ha transferido a '{pokemon.nombre}' al Profesor Oak.")

    def deshacer_transferencia(self):
        pokemon = self.transferencias.desapilar()
        if pokemon is None:
            print("No hay transferencias para deshacer.")
            return
        self.pc.insertar_al_inicio(pokemon)
        print(f"'{pokemon.nombre}' ha vuelto a la PC.")