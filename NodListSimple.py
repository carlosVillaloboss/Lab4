class NodoSimple:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaSimple:
    def __init__(self):
        self.cabeza = None
        self.size = 0

    def size(self):
        return self.size

    def isEmpty(self):
        return self.cabeza is None

    def addFirst(self, dato):
        nuevo_nodo = NodoSimple(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        self.size += 1

    def addLast(self, dato):
        nuevo_nodo = NodoSimple(dato)
        if self.isEmpty():
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.size += 1

    def removeFirst(self):
        if self.isEmpty():
            print("La lista está vacía.")
            return None
        else:
            nodo_eliminado = self.cabeza
            self.cabeza = self.cabeza.siguiente
            self.size -= 1
            return nodo_eliminado.dato

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato)
            actual = actual.siguiente
        print("None")

