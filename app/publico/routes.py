from . import publico_bp
from .models import Categoria

from flask import render_template

@publico_bp.route("/")
def index():
    return render_template("publico/index.html")

@public_bp.route("/posts")
def posts():
    pass