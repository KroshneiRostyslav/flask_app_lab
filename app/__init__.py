from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name="development"):
    app = Flask(__name__)

    from app.config import (
        DevelopmentConfig,
        TestingConfig,
        ProductionConfig
    )

    configs = {
        "development": DevelopmentConfig,
        "testing": TestingConfig,
        "production": ProductionConfig
    }

    app.config.from_object(configs[config_name])

    db.init_app(app)
    migrate.init_app(app, db)

    from app.posts import post_bp
    
    app.register_blueprint(
        post_bp,
        url_prefix="/posts"
    )

    from app.posts.models import Post
    from app.posts.users import User    

    @app.errorhandler(404)
    def not_found(error):
        return render_template("404.html"), 404

    return app