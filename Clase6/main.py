from Estructuras.Lista import Lista
from Curso import Curso
from Alumno import Alumno

if __name__== "__main__":
    coloresConsola = {
        'azul': '\033[94m',
        'verde': '\033[92m',
        'rojo': '\033[91m',
        'fin': '\033[0m',
        'negrita': '\033[1m',
        'amarillo': '\033[93m',
        'morado': '\033[95m'
    }

    print(coloresConsola['negrita'] + coloresConsola['rojo'] + "Clase # 6 - 01/03-2024" + coloresConsola['fin'])
    
    listaCursos = Lista()


    curso1 = Curso(770, "IPC1", "A", "101", None)
    curso2 = Curso(771, "IPC2", "B", "102", None)
    curso3 = Curso(772, "EDD", "C", "103", None)

    listaCursos.insertar(curso1)
    listaCursos.insertar(curso2)
    listaCursos.insertar(curso3)


    print(coloresConsola['negrita'] + coloresConsola['azul'] + "\nListado de Cursos Disponibles: " + coloresConsola['fin'])
    listaCursos.imprimir()

    print(coloresConsola['negrita'] + coloresConsola['verde'] + "\nIngrese el código del curso para agregar alumnos: " + coloresConsola['fin'])
    cantidadAlumnosAGuardar = 0

    try:
        codigoCurso = int(input())
        print(coloresConsola['negrita'] + coloresConsola['verde'] + "\nIngrese la cantidad de alumnos a guardar: " + coloresConsola['fin'])
        cantidadAlumnosAGuardar = int(input())

        cursoEncontrado = listaCursos.buscar(codigoCurso)

        if cursoEncontrado != None:
            print(coloresConsola['negrita'] + coloresConsola['verde'] + f"\nCurso encontrado: {cursoEncontrado}" + coloresConsola['fin'])
            for i in range(cantidadAlumnosAGuardar):
                print( coloresConsola['amarillo'] + "Ingrese el nombre del alumno: " + coloresConsola['fin'])
                nombreAlumno = input()
                print(coloresConsola['amarillo'] + "Ingrese el carnet del alumno: " + coloresConsola['fin'])
                carnetAlumno = input()
                print(coloresConsola['amarillo'] + "Ingrese la nota del alumno: " + coloresConsola['fin'])
                notaAlumno = int(input())

                alumno = Alumno(nombreAlumno, carnetAlumno, notaAlumno)

                if cursoEncontrado.estudiantes == None:
                    cursoEncontrado.estudiantes = Lista()
                cursoEncontrado.estudiantes.insertar(alumno)

                print(coloresConsola['negrita'] + coloresConsola['verde'] + f"\nAlumno agregado: {alumno}" + coloresConsola['fin'])
        else:
            print(coloresConsola['negrita'] + coloresConsola['rojo'] + "Error: No se encontró el curso" + coloresConsola['fin'])
            exit()
    except ValueError:
        print(coloresConsola['negrita'] + coloresConsola['rojo'] + "Error: Ingrese un número entero" + coloresConsola['fin'])
    except Exception as e:
        print(coloresConsola['negrita'] + coloresConsola['rojo'] + "Error: " + str(e) + coloresConsola['fin'])

    # Busqueda dentro de una lista interna:
    print(coloresConsola['negrita'] + coloresConsola['verde'] + "\nIngrese el código del curso para buscar a un alumno en específico: " + coloresConsola['fin'])
    codigoCursoIngresado = int(input())
    alumnoActual = None
    try:
        cursoSeleccionado = listaCursos.buscar(codigoCursoIngresado)
        if cursoSeleccionado is not None:
            print(coloresConsola['negrita'] + coloresConsola['verde'] + f"Ingrese el carnet del alumno: " + coloresConsola['fin'])
            carnetIngresado = input()

            alumnoActual = cursoSeleccionado.estudiantes.buscarAlumno(carnetIngresado)

            if alumnoActual is not None:
                print(coloresConsola['negrita'] + coloresConsola['verde'] + f"Alumno encontrado: {alumnoActual}" + coloresConsola['fin'])
            else:
                print(coloresConsola['negrita'] + coloresConsola['rojo'] + "Error: No se encontró el alumno" + coloresConsola['fin'])
        else:
            print(coloresConsola['negrita'] + coloresConsola['rojo'] + "Error: No se encontró el curso" + coloresConsola['fin'])
    except ValueError:
        print(coloresConsola['negrita'] + coloresConsola['rojo'] + "Error: Ingrese un número entero" + coloresConsola['fin'])
    except Exception as e:
        print(coloresConsola['negrita'] + coloresConsola['rojo'] + "Error: " + str(e) + coloresConsola['fin'])


    print(coloresConsola['negrita'] + coloresConsola['morado'] + "\nIngrese el código del curso para ordenar a los alumnos por nota: " + coloresConsola['fin'])
    codigoCursoIngresado = int(input())

    try:
        cursoSeleccionado = listaCursos.buscar(codigoCursoIngresado)
        if cursoSeleccionado is not None:
            cursoSeleccionado.estudiantes.BubbleSort()
            cursoSeleccionado.estudiantes.BubbleDescendente()
        else:
            print(coloresConsola['negrita'] + coloresConsola['rojo'] + "Error: No se encontró el curso" + coloresConsola['fin'])
    except ValueError:
        print(coloresConsola['negrita'] + coloresConsola['rojo'] + "Error: Ingrese un número entero" + coloresConsola['fin'])
