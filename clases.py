#archivo para  guardar las clases que se van a utilizar en el proyecto

import json

class Pokemon:
    """implemento la clase pokemon del modulo 1"""

    def __init__(self, id, nombre, tipo, poder_combate):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.poder_combate = poder_combate

    def __str__(self):
        return f"#{self.id:03d} {self.nombre} (Tipo: {self.tipo}, PC: {self.poder_combate})"
    

#clase que funciona como base de datos donde se guardan todos los pokemones utilizando has map
class Pokedex:

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
    
#registro de los nombres de las medallas

import json


class RegistroMedallas:

    def __init__(self, archivo_json=None):
        self.medallas = set()
        if archivo_json:
            self._cargar_desde_json(archivo_json)


    def _cargar_desde_json(self, archivo_json):
        with open(archivo_json, "r", encoding="utf-8") as f:
            datos = json.load(f)
        for medalla in datos:
            self.medallas.add(medalla)

    def agregar_medalla(self, nombre_medalla):
        if nombre_medalla in self.medallas:
            print(f"Ya posees la '{nombre_medalla}'. No se puede duplicar.")
            return False
        self.medallas.add(nombre_medalla)
        print(f"¡Has obtenido la '{nombre_medalla}'!")
        return True

    def listar(self):
        return sorted(self.medallas)

