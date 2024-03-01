from .Nodo import Nodo

class Lista:
    def __init__(self):
        self.primero = None
        self.size = 0

    def insertar(self, dato):
        nuevo = Nodo(dato) # Creamos un nuevo nodo

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

    def buscar(self, codigoIngresado):
        actual = self.primero
        while actual != None:
            if actual.dato.codigo == codigoIngresado:
                return actual.dato
            actual = actual.siguiente
        return None
    
    def buscarAlumno(self, carnetIngresado):
        actual = self.primero
        while actual != None:
            if actual.dato.carnet == carnetIngresado:
                return actual.dato
            actual = actual.siguiente
        return None

    # Bubblesort
    def BubbleSort(self):
        if self.primero is None or self.primero.siguiente is None:
            return 

        last = None
        while last != self.primero:
            actual = self.primero
            while actual.siguiente != last:
                if actual.dato.nota > actual.siguiente.dato.nota:
                    actual.dato, actual.siguiente.dato = actual.siguiente.dato, actual.dato
                actual = actual.siguiente
            last = actual

        print("Lista ordenada: ")
        self.imprimir()
                
    # InsertionSort
    
    def insertionSort(self):
        if self.primero is None or self.primero.siguiente is None:
            return
        
        actual = self.primero.siguiente
        while actual != None:
            actual2 = self.primero
            while actual2 != actual:
                if actual.dato.nota < actual2.dato.nota:
                    actual.dato, actual2.dato = actual2.dato, actual.dato
                actual2 = actual2.siguiente
            actual = actual.siguiente

        print("Lista ordenada:")
        self.imprimir()

        print("Lista ordenada: ")
        self.imprimir()

        
    #Orden Alfabético:
    def BubbleDescendente(self):
        if self.primero is None or self.primero.siguiente is None:
            return 

        last = None
        while last != self.primero:
            actual = self.primero
            while actual.siguiente != last:
                if actual.dato.nombre > actual.siguiente.dato.nombre:
                    actual.dato, actual.siguiente.dato = actual.siguiente.dato, actual.dato
                actual = actual.siguiente
            last = actual

        print("Lista: ")
        self.imprimir()