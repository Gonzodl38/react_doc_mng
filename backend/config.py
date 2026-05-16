import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Priority:
    # 1. DATABASE_URL env var (full control, e.g. MySQL in your PC)
    # 2. Fallback to SQLite (for portable deployments)

    DATABASE_URL = os.getenv("DATABASE_URL")

    if DATABASE_URL:
        SQLALCHEMY_DATABASE_URI = DATABASE_URL
    else:
        SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "doc_management.db")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "dev")