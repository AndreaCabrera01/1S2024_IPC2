class Curso:
    def __init__(self, nombre, seccion, aula, estudiantes):
        self.nombre = nombre
        self.seccion = seccion
        self.aula = aula
        self.estudiantes = estudiantes

    def __str__(self):
        return f'Curso: {self.nombre}, Sección: {self.seccion}, Aula: {self.aula}'
    
    def promedio(self):
        suma = 0
        for est in self.estudiantes:
            suma += est.nota
        return suma/len(self.estudiantes)
    