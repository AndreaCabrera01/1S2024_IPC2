from Estructuras.ListaEnlazada.ListaEnlazada import ListaEnlazada
from Estructuras.ListaDEnlazada.ListaDEnlazada import ListaDEnlazada
from Estructuras.ListaCircular.ListaCircular import listaCircular
from Estructuras.ListaDCircular.ListaDCircular import ListaDCircular

from Persona import Persona

if __name__ == "__main__":


    print("--------LISTA ENLAZADA--------")
    listaEnlazadaEj = ListaEnlazada()
    listaEnlazadaEj.insertar(10)
    listaEnlazadaEj.insertar(20)
    listaEnlazadaEj.insertar(30)
    listaEnlazadaEj.insertar("Andrea")

    listaEnlazadaEj.imprimir()

    print("--------LISTA DOBLEMENTE ENLAZADA--------")
    listaDEn = ListaDEnlazada()
    listaDEn.insertar("manzana")
    listaDEn.insertar("banano")
    listaDEn.insertar("naranja")

    listaDEn.imprimir()
    print("")
    listaDEn.imprimirReversa()

    print("--------LISTA CIRCULAR--------")
    listaC = listaCircular()
    listaC.insertar("Perro")
    listaC.insertar("Gato")
    listaC.insertar("Ratón")

    listaC.imprimir()
    print("")

    print("--------LISTA DOBLEMENTE CIRCULAR--------")
    listaDC = ListaDCircular()
    listaDC.insertar("Andrea")
    listaDC.insertar("María")
    listaDC.insertar("Pepito")
    listaDC.insertar("Fulano")
    listaDC.imprimir()
    print()

    print("--------LISTA DE OBJETOS--------")
    Persona1 = Persona("Juan", 22)
    Persona2 = Persona("Luis", 21)
    Persona3 = Persona("Pedro", 24)

    listaPersonas = ListaEnlazada()
    listaPersonas.insertar(Persona1)
    listaPersonas.insertar(Persona2)
    listaPersonas.insertar(Persona3)    

    listaPersonas.imprimir() #Imprimir la dirección de memoria
                            # Para resolver esto, hacemos: 1) Sobreescribir el método __str__ en el objeto Persona
                            # Modificar en la lista la impresion.
    print( )
    listaPersonas.imprimirPersona()