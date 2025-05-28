# Flask API routes

from flask import Blueprint, jsonify

routes = Blueprint('routes', __name__)

@routes.route('/api/updates')
def get_updates():
    return jsonify({'status': 'OK', 'data': []})
