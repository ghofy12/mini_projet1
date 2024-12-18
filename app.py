from flask import Flask, jsonify, request

app = Flask(__name__)

# Exemple de données statiques
candidates = [
    {"id": 1, "name": "Alice", "position": "Developer"},
    {"id": 2, "name": "Bob", "position": "Designer"},
    {"id": 3, "name": "Charlie", "position": "Manager"}
]

# Endpoint pour récupérer tous les candidats
@app.route('/candidates', methods=['GET'])
def get_candidates():
    return jsonify(candidates), 200

# Endpoint pour récupérer un candidat par son ID
@app.route('/candidates/<int:id>', methods=['GET'])
def get_candidate(id):
    candidate = next((c for c in candidates if c['id'] == id), None)
    if candidate is None:
        return jsonify({"message": "Candidate not found"}), 404
    return jsonify(candidate), 200

# Endpoint pour ajouter un nouveau candidat
@app.route('/candidates', methods=['POST'])
def add_candidate():
    new_candidate = request.get_json()
    candidates.append(new_candidate)
    return jsonify(new_candidate), 201

# Démarrer l'application
if __name__ == '__main__':
    app.run(debug=True)
