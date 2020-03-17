from . import categorias_bp
from .models import Categoria


@categorias_bp.route("/crearCategoria/<string:nombre>")
def index(nombre):
    c = Categoria(nombre=nombre)
    c.save()
    return "Categoria insertada correctamente:<br>"+str(repr(c))