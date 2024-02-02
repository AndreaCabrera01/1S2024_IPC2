#Funcion Suma
def sumaFunc(num1, num2):
    return num1 + num2

#Funcion Resta
def restaFunc(num1, num2):
    return num1 - num2

#Funcion Multiplicación
def multiFunc(num1, num2):
    return num1 * num2

#Función de División
def divFunc(num1, num2):
    return num1 / num2

def Menu():
    print ('Que operacion quieres hacer?')
    print ('1. Suma')
    print ('2. Resta')
    print ('3. Multiplicacion')
    print ('4. Division')
    print ('5. Salir')
    opcion = input()
    return opcion


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
    b = 3 # entero

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

    print('Hola ' + nombre + ' su edad es:', int(edad))

    # Condicionales
    # IF:
    if a == 1:
        print('Si, "a" posee el valor de 1.')
    else:
        print('No, "a" no es igual a 1.')

    # Operadores lógicos:
    # Python: and, or, not ----------------- Java: &&, ||, !
    
    if a == 1 and b == 2:
        print('Si se cumple con las condiciones')
    elif a == 2 or int(edad) == 22:
        print('Se cumple alguna de las condiciones')
    elif not a == 1:
        print('se cumple con que a NO es 1')
    else:
        print('Ninguna de las condiciones se cumple.')
    

    # Operadores de Comparación
    # ==, !=, <, >, <=, >=
    # igual que, no es igual, menor qué, mayor qué, menor igual qué, mayor igual qué:
        
    if int(edad) >= 18:
        print('MAYOR DE EDAD')
    else:
        print('MENOR DE EDAD')


    #Ciclos:
    # FOR:
    for i in range(0,10):
        print(i)

    # WHILE:
    print('CONTADOR CON WHILE: ')
    contador = 0
    while contador < 10:
        print(contador)
        contador += 1
    
    # Funciones:
    print('SUMA', sumaFunc(1, 89))
    print('RESTA', restaFunc(2, 6))
    print('MULTIPLICACIÓN', multiFunc(2, 8))
    print('DIVISIÓN', divFunc(8, 4))

    #Saltos de Línea
    print()
    print('\n')

    # listas:
    lista = [1,2,3]
    print(lista)

    '''
    JAVA:

    for(int i = 0; i < lista.length; i++){
        System.out.println(lista[i]);
    }
    '''


    for i in lista:
        print(i)

    
    print('Por posición:')
    for pos in range(0, len(lista)):
        print(lista[pos])

    opcion = Menu()
    while opcion != '5':
        num1 = int(input('Ingresa el primer número: '))
        num2 = int(input('Ingresa el segundo número: '))

        if opcion == '1':
            print('La suma es: ' + str(sumaFunc(num1, num2)))
        elif opcion == '2':
            print('La resta es: ' + str(restaFunc(num1, num2)))
        elif opcion == '3':
            print('La multiplicación es: ' + str(multiFunc(num1, num2)))
        elif opcion == '4':
            print('La división es: ' + str(divFunc(num1, num2)))
        else: 
            print('Opción no válida')
        opcion = Menu()

    print('Adiós, gracias por usar la calculadora')