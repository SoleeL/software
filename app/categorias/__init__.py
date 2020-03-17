from flask import Blueprint

categorias_bp = Blueprint('categorias', __name__, template_folder='templates', static_folder='static')

from . import routes
