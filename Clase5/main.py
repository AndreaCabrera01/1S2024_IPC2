import re

if __name__ == '__main__':
    #Ficheros:
    # Apertura de ficheros:

    archivo = open('fichero.txt', 'w') # Modo de apertura es 'w' -> escritura, se sobreescribe si el fichero ya existe
    archivo.write("Soy Andrea, mi carnet es 123") # Escritura
    archivo.close() # Cerrar

    archivo = open('fichero.txt', 'r') # r -> lectura
    contenido = archivo.read() # Obteniendo el contenido dentro del fichero
    print(contenido)
    archivo.close()

    # Escritura de ficheros:
    archivo = open('fichero.txt', 'a') #modo add, para agregar al final
    archivo.write('\n Hola a todos')
    archivo.close()

    # utilización de with para abrir y cerrar ficheros:
    with open('fichero.txt', 'w') as archivo:
        archivo.write("Desde with")

    # MANEJO DE EXCEPCIONES:
    try:
        with open('ficheroNoExistente.txt', 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print("Este fichero no existe :[")
    except Exception as e:
        print("Error inesperado: ", e)

    # Tuplas:
    tupla = (1,2,3,4,5) # Creacion
    print(tupla)
    print(tupla[0])
    print(tupla[1:3])
    print(tupla[1:])
    print(tupla[:3])
    print(tupla[-1])
    
    # Diccionarios:
    diccionario = {'nombre': 'Juan', 'edad': 28, 'cursos': ['Python', 'Java', 'Javascript']}

    print(diccionario)
    print(diccionario['nombre'])

    # REGEX:
    texto = 'En esta cadena se encuentra una palabra mágica'
    patron = 'mágica'

    print(re.search(patron, texto))

    txt = 'yo tengo 22 años'
    x = re.findall('\d', txt)
    print(x)

    txt2 = 'La lluvia en Sevilla es una maravilla'
    y = re.findall('a', txt2)
    print(len(y))