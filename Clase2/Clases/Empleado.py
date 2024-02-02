from Clases.Persona import Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad) # Llamamos al constructor de la clase Padre
        self.salario = salario
        self.__userEmployee = None

    def __str__(self):
        return f'Empleado: {self.nombre}, {self.edad}, SALARIO: {self.salario}'
    
    def setUserEmployee(self, user): #SETTER
        self.__userEmployee = user

    def getUserEmployee(self): #GETTER
        return self.__userEmployee
    

    def trabajar(self):
        return f'{self.nombre} está trabajando'
    
    def cobrar(self):
        return f'{self.nombre} está cobrando su salario'
