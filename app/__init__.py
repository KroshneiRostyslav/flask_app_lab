from flask import Flask, render_template
import os

app = Flask(__name__)
app.secret_key = b'secret_key'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config.from_pyfile(os.path.join(basedir, "..", "config.py"))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

from .users import users_bp
from .products import products_bp
app.register_blueprint(users_bp)
app.register_blueprint(products_bp)