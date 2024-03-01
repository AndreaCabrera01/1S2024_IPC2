class Alumno:
    def __init__(self, nombre, carnet, nota):
        self.nombre = nombre
        self.carnet = carnet
        self.nota = nota

    def __str__(self):
        return f'Alumno: {self.nombre} -  {self.carnet}, Nota: {self.nota}'