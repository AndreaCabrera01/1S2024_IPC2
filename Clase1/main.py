if __name__ == '__main__':
    print('Hola, estoy en el main')

    # Este es un comentario de 1 línea
    '''
    Hola este es el comentario multilinea
    linea1
    linea2
    '''

    # Variables:
    x = '''
    hola 
    soy 
    el string
    '''

    a = 1 # entero
    b = 2 # entero

    c = 1.0 # flotante
    d = 2.0 # flotante

    e = "doble"
    f = 'simples'

    # ejemplo = true <-- está mal
    g = True # boolean
    h = False # boolean

    # Operaciones:
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b

    # impresiones:
    print(suma)
    print(resta)
    print(multiplicacion)
    print(division)

    # Obtener input de un usuario:
    print('Ingrese su nombre: ')
    nombre = input()

    edad = input('Ingrese su edad: ')

    print('Hola ' + nombre + ' su edad es:', edad)

    # Condicionales
