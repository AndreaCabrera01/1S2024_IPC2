import xml.etree.ElementTree as ET # Importar librería ElementTree
from xml.dom import minidom # Importar librería minidom
from Curso import Curso # Importar la clase Curso
from Estudiante import Estudiante # Importar la clase Estudiante


listaCursos = [] # Lista vacia de cursos    
def Menu():
    print(' ------------- Menu Principal -------------')
    print('1. Leer archivo XML (ElementTree)')
    print('2. Leer archivo XML (minidom)')
    print('3. Escribir archivo XML (ElementTree - XML con información del curso y promedio de notas de los estudiantes)')
    print('4. Escribir archivo XML (minidom -  XML con información del curso y promedio de notas de los estudiantes)')
    print('5. LIMPIAR DATOS ')
    print('6. Salir')
    print(' ------------------------------------------')

    opc = int(input('Ingrese una opción: '))
    return opc


def LeerArchivoET(rutaArchivo):
    tree = ET.parse(rutaArchivo) #Parsear el archivo XML
    root = tree.getroot() # Obtenemos la raíz, en este caso <cursosSistemas>
    #print('RAIZ: ', root.tag)

    for curso_elem in root.findall('curso'): #iterar
        nombreCurso = curso_elem.get('nombre') # obtenemos el atributo de nombre.
        seccionCurso = curso_elem.find('seccion').text
        aulaCurso = curso_elem.find('aula').text

        curso = Curso(nombreCurso, seccionCurso, aulaCurso, [])

        for estudiante_elem in curso_elem.find('estudiantes').findall('estudiante'):
            nombreEstudiante = estudiante_elem.find('nombre').text
            apellidoEstudiante = estudiante_elem.find('apellido').text
            carnetEstudiante = estudiante_elem.find('carnet').text
            notaEstudiante = float(estudiante_elem.find('nota').text)

            estudiante = Estudiante(nombreEstudiante, apellidoEstudiante, carnetEstudiante, notaEstudiante)
            curso.estudiantes.append(estudiante)

        listaCursos.append(curso)

    print("SE HA LEIDO LA INFORMACIÓN DEL XML")
    for c in listaCursos:
        print('\n', c)
        for e in c.estudiantes:
            print('\t', e.nombre, e.apellido, e.carnet, e.nota)

def LeerArchivoMD(rutaArchivo):
    doc = minidom.parse(rutaArchivo) # Parsear el archivo XML
    root = doc.documentElement # Obtener el nodo raíz, en este caso <cursosSistemas>
    cursos = root.getElementsByTagName('curso') # Obtener los nodos curso

    for curso in cursos:
        nombreCurso = curso.getAttribute('nombre') # Obtener el atributo nombre del nodo curso
        seccionCurso = curso.getElementsByTagName('seccion')[0].firstChild.data # Obtener el texto del nodo seccion
        aulaCurso = curso.getElementsByTagName('aula')[0].firstChild.data

        cursoObj = Curso(nombreCurso, seccionCurso, aulaCurso, [])

        estudiantes = curso.getElementsByTagName('estudiantes') # Obtener los nodos estudiante
        for estudiante in estudiantes:
            nombreEstudiante = estudiante.getElementsByTagName('nombre')[0].firstChild.data #se utiliza '[0]' porque se selecciona el actual
            apellidoEstudiante = estudiante.getElementsByTagName('apellido')[0].firstChild.data
            carnetEstudiante = estudiante.getElementsByTagName('carnet')[0].firstChild.data
            notaEstudiante = float(estudiante.getElementsByTagName('nota')[0].firstChild.data)

            estudiante = Estudiante(nombreEstudiante, apellidoEstudiante, carnetEstudiante, notaEstudiante)
            cursoObj.estudiantes.append(estudiante)
        listaCursos.append(cursoObj)

def EscribirArchivoET():
    #Creando el nodo raíz
    root = ET.Element('cursosSistemas')

    #Elementos:
    for curso in listaCursos:
        curso_elem = ET.SubElement(root, 'curso')
        curso_elem.set('nombre', curso.nombre)

        seccion_elem = ET.SubElement(curso_elem, 'seccion')
        seccion_elem.text = curso.seccion

        aula_elem = ET.SubElement(curso_elem, 'aula')
        aula_elem.text = curso.aula

        promedio_element = ET.SubElement(curso_elem, 'Promedio')
        promedio_element.text = str(curso.promedio())


    tree = ET.ElementTree(root) # Crear el árbol
    tree.write('promedioPorCurso_ET.xml', encoding='utf-8', xml_declaration=True) # Escribir el archivo


def EscribirArchivoMD():
    #Con minidom:
    doc = minidom.Document() # Crear el documento
    root = doc.createElement('cursosSistemas') # Crear el nodo raíz
    doc.appendChild(root) # Agregar el nodo raíz al documento

    for curso in listaCursos:
        curso_elem = doc.createElement('curso')
        curso_elem.setAttribute('nombre', curso.nombre)

        seccion_elem = doc.createElement('seccion')
        seccion_elem.appendChild(doc.createTextNode(curso.seccion))
        curso_elem.appendChild(seccion_elem)

        aula_elem = doc.createElement('aula')
        aula_elem.appendChild(doc.createTextNode(curso.aula))
        curso_elem.appendChild(aula_elem)

        promedio_element = doc.createElement('Promedio')
        promedio_element.appendChild(doc.createTextNode(str(curso.promedio())))
        curso_elem.appendChild(promedio_element)

        root.appendChild(curso_elem)

        
    with open('promedioPorCurso_MD.xml', 'w', encoding='UTF-8') as file:
        file.write(doc.toprettyxml(indent='    ')) # Escribir el archivo y que se vea bonito

if __name__ == '__main__':
    opc = 0
    rutaArchivo = input('Ingrese la ruta de su archivo: ')
    while opc != 6:
        opc = Menu()
        if opc == 1:
            print('')
            LeerArchivoET(rutaArchivo)

        elif opc == 2:
            print('')
            LeerArchivoMD(rutaArchivo)

        elif opc == 3:
            print('')
            EscribirArchivoET()

        elif opc == 4:
            print('')
            EscribirArchivoMD()

        elif opc == 5:
            listaCursos = []
            print('Datos limpios')
        
        elif opc == 6:
            print('Adiós!')
            break
        else:
            print('Opción no válida')
        print('')
