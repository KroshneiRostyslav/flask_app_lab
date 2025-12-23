from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = b'secret_key'

app.config.from_pyfile(r'..\config.py')

@app.route("/")
def home():
    return render_template("home.html")

from .users import users_bp
from .products import products_bp
app.register_blueprint(users_bp)
app.register_blueprint(products_bp)
