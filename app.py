from flask import Flask, request, jsonify, send_from_directory
import networkx as nx
import os

app = Flask(__name__, static_folder='static')
graph = nx.DiGraph()


@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/add_relationship', methods=['POST'])
def add_relationship():
    data = request.json
    entity1 = data.get('entity1')
    relationship = data.get('relationship')
    entity2 = data.get('entity2')

    if not entity1 or not relationship or not entity2:
        return jsonify({'error': 'Missing required fields'}), 400

    graph.add_edge(entity1, entity2, relationship=relationship)
    return jsonify({'message': 'Relationship added successfully', 'entity1': entity1, 'entity2': entity2, 'relationship': relationship})


@app.route('/query', methods=['GET'])
def query_graph():
    entity = request.args.get('entity')

    if not entity:
        return jsonify({'error': 'Missing required field: entity'}), 400

    if entity not in graph:
        return jsonify({'error': f'Entity "{entity}" not found in the graph'}), 404

    response = {'entity': entity, 'relationships': []}

    # Outgoing edges
    for neighbor in graph.neighbors(entity):
        relationship = graph[entity][neighbor]['relationship']
        response['relationships'].append({'entity': neighbor, 'relationship': relationship, 'direction': 'outgoing'})

    # Incoming edges
    for predecessor in graph.predecessors(entity):
        relationship = graph[predecessor][entity]['relationship']
        response['relationships'].append({'entity': predecessor, 'relationship': relationship, 'direction': 'incoming'})

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
