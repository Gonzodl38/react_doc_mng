import os

from flask import (
    Blueprint,
    request,
    jsonify,
    current_app
)

from werkzeug.utils import secure_filename

from extensions import db

from models import Entity


entities_bp = Blueprint(
    "entities",
    __name__
)


# =========================================
# GET ENTITIES
# =========================================
@entities_bp.get("/api/entities")
def get_entities():

    entities = Entity.query.order_by(
        Entity.name
    ).all()

    return jsonify([

        {
            "id": e.id,
            "name": e.name,
            "short_name": e.short_name,
            "email": e.email,
            "phone": e.phone,
            "logo_path": e.logo_path,
            "is_centralized": e.is_centralized,
            "is_active": e.is_active,
        }

        for e in entities

    ])


# =========================================
# CREATE ENTITY
# =========================================
@entities_bp.post("/api/entities")
def create_entity():

    data = request.form

    # =========================
    # BOOLEAN FIX
    # =========================
    is_centralized = (
        data.get("is_centralized") == "true"
    )

    is_active = (
        data.get("is_active") == "true"
    )

    # =========================
    # LOGO SAVE
    # =========================
    logo_path = None

    logo = request.files.get("logo")

    if logo:

        filename = secure_filename(
            logo.filename
        )

        upload_folder = os.path.join(
            current_app.root_path,
            "uploads",
            "logos"
        )

        os.makedirs(
            upload_folder,
            exist_ok=True
        )

        save_path = os.path.join(
            upload_folder,
            filename
        )

        logo.save(save_path)

        logo_path = (
            f"uploads/logos/{filename}"
        )

    # =========================
    # CREATE ENTITY
    # =========================
    entity = Entity(

        name=data.get("name"),

        short_name=data.get(
            "short_name"
        ),

        nit=data.get("nit"),

        email=data.get("email"),

        phone=data.get("phone"),

        address=data.get("address"),

        acto_administrativo=data.get(
            "acto_administrativo"
        ),

        separator=data.get("separator"),

        is_centralized=is_centralized,

        central_dependency_code=data.get(
            "central_dependency_code"
        ),

        functions=data.get("functions"),

        logo_path=logo_path,

        is_active=is_active
    )

    db.session.add(entity)

    db.session.commit()

    return jsonify({
        "success": True,
        "id": entity.id
    })


# =========================================
# UPDATE ENTITY
# =========================================
@entities_bp.put(
    "/api/entities/<int:entity_id>"
)
def update_entity(entity_id):

    entity = Entity.query.get_or_404(
        entity_id
    )

    data = request.form

    entity.name = data.get("name")

    entity.short_name = data.get(
        "short_name"
    )

    entity.email = data.get("email")

    entity.phone = data.get("phone")

    entity.is_centralized = (
        data.get("is_centralized")
        == "true"
    )

    entity.is_active = (
        data.get("is_active")
        == "true"
    )

    db.session.commit()

    return jsonify({
        "success": True
    })


# =========================================
# DELETE ENTITY
# =========================================
@entities_bp.delete(
    "/api/entities/<int:entity_id>"
)
def delete_entity(entity_id):

    entity = Entity.query.get_or_404(
        entity_id
    )

    db.session.delete(entity)

    db.session.commit()

    return jsonify({
        "success": True
    })