from . import autentificacion_bp

from flask import request, render_template, redirect, url_for
from werkzeug.urls import url_parse

from .forms import RegistroForm
from .models import Usuario

@autentificacion_bp.route("/login")
def login():
    pass

@autentificacion_bp.route("/registro", methods=["GET","POST"])
def registro():
    form = RegistroForm()
    
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        
        usr = Usuario.obtener_por_correo(email)
        if usr is not None:
            error = "Usuario ya existe"
        else:
            usr = Usuario(name,email,password)
            usr.guardar()

            siguiente_pagina = request.args.get('next', None)
            if not siguiente_pagina or url_parse(siguiente_pagina).netloc != '':
                siguiente_pagina = url_for('autentificacion.login')
            return redirect(url_for('publico.index'))

    return render_template("autentificacion/registro.html",form=form, error=error)