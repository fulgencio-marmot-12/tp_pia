#listaenlazada


#sistema de almacenamiento de la pc con una lista enlazada(nodo y lista enlazada)

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.tamaño = 0

    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        self.tamaño += 1

    def eliminar(self, dato):
        actual = self.cabeza
        anterior = None
        while actual is not None:
            if actual.dato == dato:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self.tamaño -= 1
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

    def cargar_desde_lista_python(self, lista):
        self.cabeza = None
        self.tamaño = 0
        for elemento in reversed(lista):
            self.insertar_al_inicio(elemento)

    def esta_vacia(self):
        return self.cabeza is None

    def __len__(self):
        return self.tamaño
