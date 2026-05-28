import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
from .config import config_map
from .views import main as main_blueprint
from .posts import post_bp

load_dotenv()


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
migrate = Migrate()

def create_app(config_name: str = os.environ.get("FLASK_CONFIG", "dev")) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_map[config_name])
    print(f"Running in config: {config_name}")

    db.init_app(app)
    migrate.init_app(app, db)



    app.register_blueprint(main_blueprint)
    app.register_blueprint(post_bp)

    if config_name == "test":
        with app.app_context():
            print("Registered routes:")
            for rule in app.url_map.iter_rules():
                print(rule)

    @app.errorhandler(404)
    def not_found(e):
        return render_template('404.html'), 404

    return app
