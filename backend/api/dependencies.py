# dependencies.py

from extensions import db
from database import BaseModel


class Dependency(BaseModel):

    __tablename__ = "dependencies"

    entity_id = db.Column(
        db.Integer,
        nullable=False
    )

    dependency_name = db.Column(
        db.String(255),
        nullable=False
    )

    dependency_type = db.Column(
        db.String(255),
        nullable=True
    )