from flask import Blueprint

autentificacion_bp = Blueprint("autentificacion", __name__, template_folder="templates", static_folder="static")

from . import routes