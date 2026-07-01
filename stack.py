#archivo para implementar la stack
"""segun la consigna
Cuando el usuario decide sanar a su equipo, los Pokémon ingresan a la cola y son procesados uno por uno, simulando el tiempo de curación
"""

class stack:
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