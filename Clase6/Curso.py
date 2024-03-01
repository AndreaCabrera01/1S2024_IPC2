class Curso:
    def __init__(self, codigo, nombre, seccion, aula, estudiantes):
        self.codigo = codigo
        self.nombre = nombre
        self.seccion = seccion
        self.aula = aula
        self.estudiantes = estudiantes

    def __str__(self):
        return f'Curso: {self.codigo} -  {self.nombre}, Sección: {self.seccion}, Aula: {self.aula}'