from extensions import db

import os
from werkzeug.utils import secure_filename
from flask import current_app

class Entity(db.Model):

    __tablename__ = "entities"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(255),
        nullable=False
    )

    short_name = db.Column(
        db.String(100)
    )

    nit = db.Column(
        db.String(100)
    )

    email = db.Column(
        db.String(255)
    )

    phone = db.Column(
        db.String(100)
    )

    address = db.Column(
        db.String(255)
    )

    acto_administrativo = db.Column(
        db.Text
    )

    separator = db.Column(
        db.String(1),
        default="-"
    )

    is_centralized = db.Column(
        db.Boolean,
        default=False
    )

    central_dependency_code = db.Column(
        db.String(100)
    )

    functions = db.Column(
        db.Text
    )

    logo_path = db.Column(
        db.Text
    )

    is_active = db.Column(
        db.Boolean,
        default=True
    )