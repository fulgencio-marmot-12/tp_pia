from clases import ListaEnlazada, Stack, Queue
from clases import RegistroMedallas

TAMAÑO_MAXIMO_EQUIPO = 6
TAMAÑO_MAXIMO_TRANSFERENCIAS = 5


class Entrenador:
    def __init__(self, archivo_medallas=None):
        self.equipo_principal = []  # Array con maximo de 6
        self.pc = ListaEnlazada()
        self.centro_pokemon = Queue()
        self.transferencias = Stack(capacidad_maxima=TAMAÑO_MAXIMO_TRANSFERENCIAS)
        self.medallas = RegistroMedallas(archivo_medallas)

    def capturar_pokemon(self, pokemon):
        if len(self.equipo_principal) < TAMAÑO_MAXIMO_EQUIPO:
            self.equipo_principal.append(pokemon)
            print(f"{pokemon.nombre} se unio al equipo principal "
                  f"({len(self.equipo_principal)}/{TAMAÑO_MAXIMO_EQUIPO}).")
        else:
            print("el equipo Principal esta lleno ")
            self.pc.insertar_al_inicio(pokemon)
            print(f"derivando a Almacenamiento de PC {pokemon.nombre} añadido correctamente")

    def enviar_a_centro_pokemon(self):
        if not self.equipo_principal:
            print("no tenes Pokemon en el equipo para sanar")
            return
        for pokemon in self.equipo_principal:
            self.centro_pokemon.agregar(pokemon)
        print('enfermera Joy: "estamos curando a tus pokemon"')
        while not self.centro_pokemon.esta_vacia():
            pokemon = self.centro_pokemon.desencolar()
            print(f"procesando: [{pokemon.nombre}] sanado")
        print('enfermera Joy: "tus Pokemon estan en perfecta forma"')

    def buscar_pokemon_en_pc(self, nombre):
        for pokemon in self.pc.a_lista_python():
            if pokemon.nombre.lower() == nombre.lower():
                return pokemon
        return None

    def transferir_a_oak(self, nombre_pokemon):
        pokemon = self.buscar_pokemon_en_pc(nombre_pokemon)
        if pokemon is None:
            print("ese Pokemon no esta en la PC.")
            return
        self.pc.eliminar(pokemon)
        self.transferencias.apilar(pokemon)
        print(f"ha transferido a '{pokemon.nombre}' al Profesor Oak")

    def deshacer_transferencia(self):
        pokemon = self.transferencias.desapilar()
        if pokemon is None:
            print("no hay transferencias para deshacer")
            return
        self.pc.insertar_al_inicio(pokemon)
        print(f"'{pokemon.nombre}' volvio a la PC")