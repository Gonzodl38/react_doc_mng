from extensions import db
from sqlalchemy import UniqueConstraint


# =========================================================
# BASE MIXIN
# =========================================================
class BaseModel:
    id = db.Column(db.Integer, primary_key=True)


# =========================================================
# ENTITIES
# =========================================================
class Entity(BaseModel, db.Model):
    __tablename__ = "entities"

    name = db.Column(db.String(100), nullable=False)
    short_name = db.Column(db.String(50))
    nit = db.Column(db.String(20))

    acto_administrativo = db.Column(db.String(50))
    functions = db.Column(db.Text)

    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(100))

    is_active = db.Column(db.Boolean)
    logo_path = db.Column(db.Text)

    separator = db.Column(db.String(1))
    is_centralized = db.Column(db.Boolean)
    central_dependency_code = db.Column(db.String(15))

    representante_legal_nombre = db.Column(db.String(100))
    representante_legal_cargo = db.Column(db.String(100))

    dep_responsable_gestion_documental = db.Column(db.String(100))
    cgo_responsable_gestion_documental = db.Column(db.String(100))
    nom_responsable_gestion_documental = db.Column(db.String(100))

    # RELATIONSHIPS
    dependencies = db.relationship(
        "Dependency",
        back_populates="entity",
        cascade="all, delete-orphan",
        order_by="Dependency.code"
    )

    documental_studies = db.relationship(
        "DocumentalStudy",
        back_populates="entity",
        cascade="all, delete-orphan"
    )


# =========================================================
# DEPENDENCY
# =========================================================
class Dependency(BaseModel, db.Model):
    __tablename__ = "dependences"

    entity_id = db.Column(
        db.Integer,
        db.ForeignKey("entities.id", ondelete="CASCADE"),
        nullable=False
    )

    parent_id = db.Column(
        db.Integer,
        db.ForeignKey("dependences.id", ondelete="CASCADE")
    )

    code = db.Column(db.String(50))
    name = db.Column(db.String(200), nullable=False)
    boss_name = db.Column(db.String(45))
    boss_charge = db.Column(db.String(45))
    legal_representante = db.Column(db.Boolean, default=False, nullable=False)
    tvd_responsible = db.Column(db.Boolean, default=False, nullable=False)

    # RELATIONSHIPS
    parent = db.relationship(
        "Dependency",
        remote_side="Dependency.id",
        backref="children"
    )

    entity = db.relationship("Entity", back_populates="dependencies")

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


# =========================================================
# DEPENDENCY FUNCTIONS
# =========================================================
class DependencyFunction(BaseModel, db.Model):
    __tablename__ = "dependency_functions"

    __table_args__ = (
        UniqueConstraint('dependency_id', 'function_number', name='uq_dep_func_number'),
    )

    dependency_id = db.Column(
        db.Integer,
        db.ForeignKey("dependences.id", ondelete="CASCADE"),
        nullable=False
    )

    function_number = db.Column(db.Integer, nullable=False)
    name = db.Column(db.Text, nullable=False)

    is_non_documented = db.Column(db.Boolean, default=False, nullable=False)

    dependency = db.relationship("Dependency", back_populates="functions")


# =========================================================
# SERIES
# =========================================================
class Series(BaseModel, db.Model):
    __tablename__ = "series"

    code = db.Column(db.String(20))
    name = db.Column(db.String(255), nullable=False)
    definition = db.Column(db.String(2000))

    support = db.Column(db.String(50))

    retention_management = db.Column(db.Integer)
    retention_central = db.Column(db.Integer)

    final_disposition = db.Column(db.String(50))
    notes = db.Column(db.String(1000))

    subseries = db.relationship(
        "Subseries",
        back_populates="series",
        cascade="all, delete-orphan",
        passive_deletes=True
    )


# =========================================================
# SUBSERIES
# =========================================================
class Subseries(BaseModel, db.Model):
    __tablename__ = "subseries"

    series_id = db.Column(
        db.Integer,
        db.ForeignKey("series.id", ondelete="CASCADE"),
        nullable=False
    )

    code = db.Column(db.String(20))
    name = db.Column(db.String(1000), nullable=False)
    definition = db.Column(db.String(2000))

    support = db.Column(db.String(50))

    retention_management = db.Column(db.Integer)
    retention_central = db.Column(db.Integer)

    final_disposition = db.Column(db.String(50))
    notes = db.Column(db.String(1000))

    series = db.relationship("Series", back_populates="subseries")


# =========================================================
# DOCTYPES
# =========================================================
class Doctype(BaseModel, db.Model):
    __tablename__ = "doctypes"

    subseries_id = db.Column(
        db.Integer,
        db.ForeignKey("subseries.id", ondelete="CASCADE")
    )

    code = db.Column(db.String(50))
    name = db.Column(db.String(1000), nullable=False)
    definition = db.Column(db.String(1000), nullable=False)
    subseries = db.relationship("Subseries", backref="doctypes")


# =========================================================
# DOCUMENTAL STUDY
# =========================================================
class DocumentalStudy(BaseModel, db.Model):
    __tablename__ = "documental_studies"

    __table_args__ = (
        UniqueConstraint(
            'entity_id',
            'nombre_expediente',
            name='uq_entity_expediente'
        ),
    )

    version = db.Column(db.String(100))

    entity_id = db.Column(
        db.Integer,
        db.ForeignKey("entities.id")
    )

    dependency_id = db.Column(
        db.Integer,
        db.ForeignKey("dependences.id")
    )

    funciones_especificas = db.Column(
        db.Integer,
        db.ForeignKey("dependency_functions.id")
    )

    serie_id = db.Column(
        db.Integer,
        db.ForeignKey("series.id")
    )

    subserie_id = db.Column(
        db.Integer,
        db.ForeignKey("subseries.id")
    )

    tipo_documental_id = db.Column(
        db.Integer,
        db.ForeignKey("doctypes.id")
    )

    nombre_expediente = db.Column(db.String(255))

    non_documented = db.Column(
        db.Boolean,
        default=False
    )

    acto_administrativo = db.Column(db.String(255))
    nombre_dependencia = db.Column(db.String(255))
    nombre_grupo = db.Column(db.String(255))

    fecha_entrevista = db.Column(db.Date)

    lider_dependencia = db.Column(db.String(255))
    funcionario_entrevistado = db.Column(db.String(255))
    formalizacion_entrevista = db.Column(db.String(255))

    comentarios_entrevista = db.Column(db.Text)

    # =====================================
    # SOPORTE / FORMATO
    # =====================================
    spt_fisico = db.Column(db.String(10))
    spt_digital = db.Column(db.String(10))

    spt_url = db.Column(db.String(500))
    spt_otro = db.Column(db.String(255))
    spt_formInicial = db.Column(db.String(255))
    spt_formFinal = db.Column(db.String(255))

    # =====================================
    # TRÁMITE / RETENCIÓN
    # =====================================
    tramite_original = db.Column(db.String(100))
    tramite_copia = db.Column(db.String(100))

    tiempo_conservacion_expediente = db.Column(db.String(50))

    trd_annosOficina = db.Column(db.String(50))
    trd_annosTransfAC = db.Column(db.String(50))
    trd_perTransferencias = db.Column(db.String(50))

    disposicion_final = db.Column(db.String(20))

    # =====================================
    # SGC
    # =====================================
    sgc_nombre_proceso = db.Column(db.String(255))
    sgc_nombre_procedimiento = db.Column(db.String(255))

    # =====================================
    # ORC
    # =====================================
    orc_delegadoActAdmitivo = db.Column(db.String(255))
    orc_participante = db.Column(db.String(255))

    # =====================================
    # INFO CHARACTER
    # =====================================
    infoCaracter_publico = db.Column(db.String(5))
    infoCaracter_privado = db.Column(db.String(5))
    infoCaracter_confidencial = db.Column(db.String(5))
    infoCaracter_usoInterno = db.Column(db.String(5))

    # =====================================
    # DDHH / OBS
    # =====================================
    prodDerechosHumanos = db.Column(db.Text)
    observaciones = db.Column(db.Text)

    # =====================================
    # EXPEDIENTE
    # =====================================
    periodicidad_expediente = db.Column(db.String(100))
    volumen_documental_anno = db.Column(db.String(100))
    estado_organizacion_archivos = db.Column(db.String(255))

    nombre_software = db.Column(db.String(100))

    dependencia_grupo_tramite = db.Column(db.String(255))
    dependencia_grupo_consulta = db.Column(db.String(255))

    norma_interna = db.Column(db.String(255))
    norma_externa = db.Column(db.String(255))

    reproduccion_tecnica = db.Column(db.String(1))
    es_ddhh = db.Column(db.String(1))

    procedimiento = db.Column(db.String(255))

    # =====================================
    # RELATIONSHIPS
    # =====================================
    entity = db.relationship(
        "Entity",
        back_populates="documental_studies"
    )

    dependency = db.relationship(
        "Dependency",
        back_populates="documental_studies",
        lazy="joined"
    )

    serie = db.relationship(
        "Series",
        lazy="joined"
    )

    subserie = db.relationship(
        "Subseries",
        lazy="joined"
    )

    doctype = db.relationship(
        "Doctype",
        lazy="joined"
    )

    function = db.relationship(
        "DependencyFunction",
        lazy="joined"
    )