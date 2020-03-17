from . import app

from .categorias.models import Categoria

@app.route("/categorias/")
def categorias():
    vista = ""
    for cat in Categoria.query.all():
        vista += repr(cat) + "<br>"
    return vista
