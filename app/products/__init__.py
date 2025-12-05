from flask import Blueprint

products_bp = Blueprint(
    "products",
    __name__,
    url_prefix="/",
    template_folder="templates"
)

from . import views