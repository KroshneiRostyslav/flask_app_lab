from flask import render_template
from . import products_bp

@products_bp.route("/products")
def products():
    return render_template("products/products.html")