from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from extensions import db

db = SQLAlchemy()
migrate = Migrate()

from models import (
    Entity,
    Dependency,
    DependencyFunction,
    Series,
    Subseries,
    Doctype,
    DocumentalStudy
)


def create_app():
    app = Flask(__name__)

    # =====================================================
    # DATABASE CONFIG
    # =====================================================
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///doc_management.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # =====================================================
    # INIT EXTENSIONS
    # =====================================================
    db.init_app(app)

    return app


def create_database():
    app = create_app()

    with app.app_context():
        db.create_all()
        print("Database created successfully.")


if __name__ == "__main__":
    create_database()