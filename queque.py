#implementacion de la queue o queque

# queue hecha con lista comun, sin clase
# se usa en el centro pokemon

class queue:

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