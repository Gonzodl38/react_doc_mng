from flask import Blueprint, jsonify

from models import Entity

entities_bp = Blueprint("entities", __name__)

@entities_bp.route("/api/entities")
def get_entities():

    entities = Entity.query.all()

    return jsonify([
        {
            "id": e.id,
            "name": e.name
        }
        for e in entities
    ])