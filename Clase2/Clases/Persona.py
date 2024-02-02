class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f'Persona\nNombre: {self.nombre}, edad: {self.edad}'
        #Persona:
        #Nombre: <>, edad: <>
    #Métodos:
    def saludar(self):
        return f'Hola, yo soy {self.nombre} y tengo {self.edad} años'
    
    def despedirse(self):
        return f'Adiós, un gusto'