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