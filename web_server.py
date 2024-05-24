from flask import Flask, jsonify, Response
from sympy.geometry import entity

app = Flask(__name__)

class Entity:
    def __init__(self, id, name):
        self.id = id
        self.name = name

entities = [
    Entity(1, 'Model One'),
    Entity(2, 'Model Two'),
]

@app.route('/', methods=['GET'])
def get_entities():
    response = [ {'id': entity.id, 'name': entity.name } for entity in entities]
    return jsonify(response), 200

@app.route('/check', methods=['GET'])
def check_service():
    return jsonify({'message': 'Service is running...'}), 200

@app.route('/entity', methods=['GET'])
def get_entity(id):
    entity = next((entity for entity in entities if entity.id == id), None)
    if entity:
        return jsonify({'id': entity.id, 'name': entity.name}), 200
    else:
        return jsonify({'error': 'Entity not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)