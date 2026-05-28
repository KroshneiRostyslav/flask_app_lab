from flask import Blueprint

post_bp = Blueprint(
    "posts",
    __name__,
    url_prefix="/posts",
    template_folder="templates"
)

from . import views
