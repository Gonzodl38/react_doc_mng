# api/entities.py

from flask import (
    Blueprint,
    request,
    jsonify
)

from extensions import db

from models import Entity


entities_bp = Blueprint(
    "entities",
    __name__,
    url_prefix="/api/entities"
)


# =========================
# GET ALL ENTITIES
# =========================
@entities_bp.route(
    "/",
    methods=["GET"]
)
def get_entities():

    entities = Entity.query.all()

    return jsonify(
        [
            {
                "id": entity.id,
                "name": entity.name,
                "description": entity.description
            }
            for entity in entities
        ]
    )


# =========================
# GET ONE ENTITY
# =========================
@entities_bp.route(
    "/<int:entity_id>",
    methods=["GET"]
)
def get_entity(entity_id):

    entity = Entity.query.get_or_404(
        entity_id
    )

    return jsonify(
        {
            "id": entity.id,
            "name": entity.name,
            "description": entity.description
        }
    )


# =========================
# CREATE ENTITY
# =========================
@entities_bp.route(
    "/",
    methods=["POST"]
)
def create_entity():

    data = request.get_json()

    entity = Entity(
        name=data.get("name"),
        description=data.get("description")
    )

    db.session.add(entity)

    db.session.commit()

    return jsonify(
        {
            "message": "Entity created",
            "id": entity.id
        }
    ), 201


# =========================
# UPDATE ENTITY
# =========================
@entities_bp.route(
    "/<int:entity_id>",
    methods=["PUT"]
)
def update_entity(entity_id):

    entity = Entity.query.get_or_404(
        entity_id
    )

    data = request.get_json()

    entity.name = data.get(
        "name",
        entity.name
    )

    entity.description = data.get(
        "description",
        entity.description
    )

    db.session.commit()

    return jsonify(
        {
            "message": "Entity updated"
        }
    )


# =========================
# DELETE ENTITY
# =========================
@entities_bp.route(
    "/<int:entity_id>",
    methods=["DELETE"]
)
def delete_entity(entity_id):

    entity = Entity.query.get_or_404(
        entity_id
    )

    db.session.delete(entity)

    db.session.commit()

    return jsonify(
        {
            "message": "Entity deleted"
        }
    )


# =========================
# GET DEPENDENCIES
# =========================
@entities_bp.route(
    "/dependencies",
    methods=["GET"]
)
def get_dependencies():

    entity_id = request.args.get(
        "entity_id"
    )

    return jsonify(
        {
            "entity_id": entity_id,
            "dependencies": []
        }
    )