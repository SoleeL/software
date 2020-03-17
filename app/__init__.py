from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, static_url_path="/")
    app.config.from_object('config')
    
    db.init_app(app)
    
    from .autentificacion import autentificacion_bp
    app.register_blueprint(autentificacion_bp)
    
    from .publico import publico_bp
    app.register_blueprint(publico_bp)
    
    # solo cuando se quiere crear la base de datos con los modelos
    with app.app_context():
        db.create_all()

    return app
    
app = create_app()