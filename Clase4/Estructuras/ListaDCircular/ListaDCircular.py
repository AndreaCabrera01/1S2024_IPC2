from .NodoDC import NodoDC
class ListaDCircular:
    def __init__(self):
        self.primero = None #Inicio de la lista
        self.ultimo = None
        self.size = 0

    def insertar(self, dato):
        nuevo = NodoDC(dato=dato)
        if self.primero == None:
            self.primero = nuevo
            self.ultimo = nuevo

            #Actualizamos los punteros:
            self.ultimo.siguiente = self.primero
            self.primero.anterior = self.ultimo
        else:
            self.ultimo.siguiente = nuevo # El nodo siguiente del nodo actual es el nuevo nodo
            nuevo.anterior = self.ultimo # El nodo anterior del nuevo nodo es el actual
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.ultimo = nuevo
        self.size += 1

    def imprimir(self):
        actual = self.primero
        for i in range(self.size):
            print(actual.dato)
            actual = actual.siguiente
            i += 1