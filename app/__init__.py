from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

from sqlalchemy import MetaData

from dotenv import load_dotenv

load_dotenv()

metadata = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }
)

db = SQLAlchemy(metadata=metadata)

migrate = Migrate()

def create_app():

    app = Flask(__name__)

    app.config.from_object("app.config.Config")

    db.init_app(app)

    migrate.init_app(app, db)
    
    from app.products.models import Product, Category

    return app
