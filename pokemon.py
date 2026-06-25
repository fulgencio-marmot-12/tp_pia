import json

class Pokedex:
    #implementacion de hash map

    def __init__(self, archivo_json):
        self.registros = {}
        self._cargar_desde_json(archivo_json)

    def _cargar_desde_json(self, archivo_json):
        with open(archivo_json, "r", encoding="utf-8") as f:
            datos = json.load(f)
        for item in datos:
            pokemon = Pokemon(item["id"], item["nombre"], item["tipo"], item["poder_combate"])
            self.registros[pokemon.id] = pokemon

    def agregar(self, pokemon):
        self.registros[pokemon.id] = pokemon

    def obtener_por_id(self, id_pokemon):
        return self.registros.get(id_pokemon)

    def obtener_todos(self):
        return list(self.registros.values())

    def obtener_ids_ordenados(self):
        return sorted(self.registros.keys())
#clase del pokemon
class Pokemon:
    def __init__(self, id_pokemon: int, nombre: str, tipo: str, pc: int):
        self.id = id_pokemon
        self.nombre = nombre
        self.tipo = tipo
        self.pc = pc

    def __str__(self):
        return f"[{self.id}] {self.nombre} (Tipo: {self.tipo} | PC: {self.pc})"


class Nodo:
    def __init__(self, pokemon: Pokemon):
        self.pokemon = pokemon
        self.siguiente = None

class ListaEnlazadaPC:
    def __init__(self):
        self.cabeza = None
        
    def insertar(self, pokemon: Pokemon):
        # TODO: Implementar la lógica para agregar un Nodo al inicio o final
        pass

    def mostrar_pc(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.pokemon)
            actual = actual.siguiente
