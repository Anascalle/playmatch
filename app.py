from flask import Flask, jsonify
from flask_cors import CORS
from rawg_api import fetch_games, fetch_game_by_id, fetch_genres, fetch_platforms
import os

app = Flask(__name__)
CORS(app)  # Permitir todas las conexiones para desarrollo

@app.route('/')
def home():
    return "🎮 API de videojuegos activa en Render"

@app.route('/games', methods=['GET'])
def get_games():
    data = fetch_games()
    return jsonify(data['results'])

@app.route('/games/<int:game_id>', methods=['GET'])
def get_game_by_id(game_id):
    data = fetch_game_by_id(game_id)
    return jsonify(data)

@app.route('/genres', methods=['GET'])
def get_genres():
    data = fetch_genres()
    return jsonify(data['results'])

@app.route('/platforms', methods=['GET'])
def get_platforms():
    data = fetch_platforms()
    return jsonify(data['results'])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

