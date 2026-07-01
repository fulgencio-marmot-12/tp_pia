#implementacion de la queue o queque

class queue:
    def __init__(self):
        self.elementos = []

    def encolar(self, dato):
        self.elementos.append(dato)

    def desencolar(self):
        if self.esta_vacia():
            return None
        return self.elementos.pop(0)

    def esta_vacia(self):
        return len(self.elementos) == 0

    def __len__(self):
        return len(self.elementos)
