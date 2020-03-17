from flask import Blueprint

publico_bp = Blueprint('publico', __name__, template_folder='templates', static_folder='static')

from . import routes
