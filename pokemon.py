class Pokemon:
    def __init__(self, id_pokemon: int, nombre: str, tipo: str, pc: int):
        self.id = id_pokemon
        self.nombre = nombre
        self.tipo = tipo
        self.pc = pc

    def __str__(self):
        return f"[{self.id}] {self.nombre} (Tipo: {self.tipo} | PC: {self.pc})"

# --- ESTRUCTURAS PARA LA PC (Lista Enlazada) ---

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
