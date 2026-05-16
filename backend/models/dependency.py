class Dependency(BaseModel, db.Model):
    __tablename__ = "dependencies"

    entity_id = db.Column(
        db.Integer,
        db.ForeignKey("entities.id", ondelete="CASCADE"),
        nullable=False
    )

    parent_id = db.Column(
        db.Integer,
        db.ForeignKey("dependencies.id", ondelete="CASCADE")
    )

    code = db.Column(db.String(50))
    name = db.Column(db.String(200), nullable=False)

    boss_name = db.Column(db.String(45))
    boss_charge = db.Column(db.String(45))

    legal_representante = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )

    tvd_responsible = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )

    parent = db.relationship(
        "Dependency",
        remote_side="Dependency.id",
        backref="children"
    )

    entity = db.relationship(
        "Entity",
        back_populates="dependencies"
    )

    functions = db.relationship(
        "DependencyFunction",
        back_populates="dependency",
        cascade="all, delete-orphan"
    )

    documental_studies = db.relationship(
        "DocumentalStudy",
        back_populates="dependency",
        cascade="all, delete-orphan"
    )