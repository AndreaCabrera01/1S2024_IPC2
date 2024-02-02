from Clases.Empleado import Empleado
from Clases.Persona import Persona

def Menu():
    print(' ------------- Menu Principal -------------')
    print('1. Registrar Persona')
    print('2. Registrar Empleado')
    print('3. Mostrar Informacion')
    print('4. Opción Administrador')
    print('5. Salir')
    print(' ------------------------------------------')


if __name__ == '__main__':
    # Guardar a los objetos:
    listado = [] #Vacio

    while True:
        Menu()
        opcion = input('Ingrese una opción: ')

        if opcion == '1':
            nombre = input('Ingrese el nombre: ')
            edad = int(input('Ingrese la edad: '))

            personaCreada = Persona(nombre, edad)
            listado.append(personaCreada)

        elif opcion == '2':
            nombre = input('Ingrese el nombre: ')
            edad = int(input('Ingrese la edad: '))
            salario = float(input('Ingrese el salario: '))

            empleadoCreado = Empleado(nombre, edad, salario)
            listado.append(empleadoCreado)

        elif opcion == '3':
            print()
            print("IMPRESIÓN DE DATOS: ")
            for i in listado:
                print(i)
                if isinstance(i, Empleado):
                    print(i.trabajar())
                    print(i.cobrar())
                print('---------------------')
        
        elif opcion == '4':
            print()
            print('OPCIÓN ADMINISTRADOR: ')
            print('ingrese su usuario y contraseña: ')
            user = input('Usuario: ')
            password = input('Contraseña: ')

            if user == 'admin' and password == '1234':
                print('Bienvenido Administrador')
                print()

                if len(listado) == 0:
                    print('No hay ningún registro')
                    break
                else:
                    for obj in listado:
                        if isinstance(obj, Empleado):
                            userEmployee = input(f'Ingrese el usuario para {obj.nombre}: ')
                            obj.setUserEmployee(userEmployee)
                    print('Usuario asignado Correctamente')
                    print(obj.getUserEmployee())
            else:
                print('Usuario o contraseña incorrectos')
        
        elif opcion == '5':
            print('Gracias por usar el programa')
            break

        else:
            print('Opción no válida')