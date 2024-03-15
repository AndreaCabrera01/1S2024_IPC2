from NodoLE import NodoLE

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.size = 0

    def insertar(self, dato):

        nuevo = NodoLE(dato) # Crea un nuevo nodo
        if self.primero == None: # Si la lista está vacía
            self.primero = nuevo # El nuevo nodo es el primero
        else: # Si la lista no está vacía
            actual = self.primero # Se crea un nodo actual que apunta al primero
            while actual.siguiente != None: # Mientras el nodo actual tenga un nodo siguiente
                actual = actual.siguiente # El nodo actual se mueve al siguiente
            actual.siguiente = nuevo # El nodo siguiente del nodo actual es el nuevo nodo
        
        self.size += 1 # Aumenta el tamaño de la lista

    def buscar(self, dato):
        actual = self.primero

        while actual != None:
            if actual.dato.nombre == dato:
                return actual.dato
            actual = actual.siguiente
        return None
    
    def imprimir(self):
        actual = self.primero
        while actual != None:
            print(actual.dato)
            actual = actual.siguiente

