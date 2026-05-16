from flask import (
    Flask,
    send_from_directory
)

from flask_cors import CORS

from config import Config

from extensions import (
    db,
    migrate
)


def create_app():

    app = Flask(__name__)

    app.config.from_object(
        Config
    )

    CORS(app)

    db.init_app(app)

    migrate.init_app(app, db)

    # =========================
    # BLUEPRINTS
    # =========================
    from api.entities import (
        entities_bp
    )

    app.register_blueprint(
        entities_bp
    )

    # =========================
    # HOME
    # =========================
    @app.route("/")
    def home():

        return {
            "message": "Backend online"
        }

    # =========================
    # LOGO FILES
    # =========================
    @app.route(
        "/uploads/logos/<filename>"
    )
    def uploaded_logo(filename):

        return send_from_directory(
            "uploads/logos",
            filename
        )

    return app


app = create_app()


if __name__ == "__main__":

    app.run(debug=True)