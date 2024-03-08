from flask import Flask, jsonify, request
from flask_cors import CORS
from animal import Animal

app = Flask(__name__)
CORS(app)

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

    return jsonify({'mensaje': 'Animal creado', 'animal': {
        'nombre': animal.nombre,
        'edad': animal.edad,
        'raza': animal.raza
    }})


if __name__ == '__main__':
    app.run(debug=True, port=5000)