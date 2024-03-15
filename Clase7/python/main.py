from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from animal import Animal

app = Flask(__name__)
CORS(app)
listadoAnimales = []
# RUTAS:
@app.route('/')
def index():
    return 'Hola mundo'

@app.route('/api', methods=['GET'])
def api():
    return jsonify({'mensaje': 'Hola mundo'})

@app.route('/api/suma', methods=['POST'])
def suma():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    return jsonify({'resultado': num1 + num2})

@app.route('/api/animal', methods=['POST'])
def animal():
    data = request.get_json()
    nombre = data['nombre']
    edad = data['edad']
    raza = data['raza']
    animal = Animal(nombre, edad, raza)

    listadoAnimales.append(animal)


    return jsonify({'mensaje': 'Animal creado', 'animal': {
        'nombre': animal.nombre,
        'edad': animal.edad,
        'raza': animal.raza
    }})

@app.route('/api/animal/<nombre>', methods=['GET'])
def animalNombre(nombre):
    encontrado = False
    for animal in listadoAnimales:
        if animal.nombre == nombre:
            encontrado = True
            return f'''
                <h1> Este es el ejemplo del 15/03 </h1>
                <h2> Nombre: {animal.nombre} </h2>
                <h2> Edad: {animal.edad} </h2>
                <h2> Raza: {animal.raza} </h2>
            '''
    
    if not encontrado:
        return jsonify({'mensaje': 'Animal no encontrado'})

@app.route('/api/animal/test', methods=['GET'])
def test():
    return render_template('index.html', content='Hola soy Andrea')


if __name__ == '__main__':
    app.run(debug=True, port=5000)