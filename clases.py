#archivo para  guardar las clases que se van a utilizar en el proyecto

import json


#sistema de almacenamiento de la pc con una lista enlazada(nodo y lista enlazada)

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0

    def insertar_al_inicio(self, dato):
        nodo_nuevo = Nodo(dato)
        nodo_nuevo.siguiente = self.cabeza
        self.cabeza = nodo_nuevo
        self.tamanio += 1

    def eliminar(self, dato):
        actual = self.cabeza
        anterior = None

        while actual is not None:
            if actual.dato == dato:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self.tamanio -= 1
                return True
            anterior = actual
            actual = actual.siguiente

        return False

    def a_lista_python(self):
        resultado = []
        actual = self.cabeza
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    def cargar_desde_lista(self, lista):
        self.cabeza = None
        self.tamanio = 0
        i = len(lista) - 1
        while i >= 0:
            self.insertar_al_inicio(lista[i])
            i -= 1

    def esta_vacia(self):
        return self.cabeza is None

#archivo para implementar la stack
"""segun la consigna
Cuando el usuario decide sanar a su equipo, los pokemon ingresan a la cola y son procesados uno por uno, simulando el tiempo de curación
"""

class Stack:
    def __init__(self, capacidad_maxima=None):
        self.elementos = []
        self.capacidad_maxima = capacidad_maxima

    def apilar(self, dato):
        if self.capacidad_maxima is not None and len(self.elementos) >= self.capacidad_maxima:
            self.elementos.pop(0)
        self.elementos.append(dato)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.elementos.pop()

    def esta_vacia(self):
        return len(self.elementos) == 0

    def __len__(self):
        return len(self.elementos)

#implementacion de la queue o queque

# queue hecha con lista comun, sin clase
# se usa en el centro pokemon

class Queue:

    def __init__(self):
        self.elementos = []

    def agregar(self, dato):
        self.elementos.append(dato)

    def sacar(self):
        if self.esta_vacia():
            return None
        return self.elementos.pop(0)

    def esta_vacia(self):
        return len(self.elementos) == 0

    def __len__(self):
        return len(self.elementos)
    
class Pokemon:
    """implemento la clase pokemon del modulo 1"""

    def __init__(self, id, nombre, tipo, poder_combate):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.poder_combate = poder_combate

    def __str__(self):
        return f"#{self.id:03d} {self.nombre} (Tipo: {self.tipo}, PC: {self.poder_combate})"
    
#hash set
class RegistroMedallas:
    def __init__(self, archivo_json=None):
        self.medallas = set() # el set
        if archivo_json:
            self.cargar_desde_json(archivo_json)

    def cargar_desde_json(self, archivo_json):
        with open(archivo_json, "r", encoding="utf-8") as f:
            datos = json.load(f)
        for medalla in datos:
            self.medallas.add(medalla)

    def agregar_medalla(self, nombre_medalla):
        if nombre_medalla in self.medallas:
            print(f"ya tenes la '{nombre_medalla}', no se puede duplicar")
            return False
        self.medallas.add(nombre_medalla)
        print(f"has obtenido la '{nombre_medalla}'")
        return True

    def mostrar(self):
        return sorted(self.medallas)

# base de datos donde se guardan todos los pokemones utilizando hash map

class Pokedex:

    def __init__(self, archivo_json):
        self.registros = {}
        self.cargar_desde_json(archivo_json)

    def cargar_desde_json(self, archivo_json):
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