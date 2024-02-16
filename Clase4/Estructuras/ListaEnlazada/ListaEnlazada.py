from .NodoLE import NodoLE

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.size = 0

    def insertar(self, dato):
        nuevo = NodoLE(dato) # Creamos un nuevo nodo

        if self.primero == None: #Si la lista está vacía
            self.primero = nuevo

        else: # Si la lista no está vacía
            actual = self.primero # Obtenemos el primero de la lista
            while actual.siguiente != None: # Mientras el nodo actual tenga un nodo siguiente
                actual = actual.siguiente  # El nodo actual se mueve al siguiente
            actual.siguiente = nuevo # Se agrega el nodo
        self.size += 1

    def imprimir(self):
        actual = self.primero
        while actual.siguiente != None:
            print(actual.dato)
            actual = actual.siguiente

        print(actual.dato)

    def imprimirPersona(self):
        actual = self.primero
        while actual.siguiente != None:
            print(actual.dato.nombre, actual.dato.edad)
            actual = actual.siguiente

        print(actual.dato.nombre, actual.dato.edad)