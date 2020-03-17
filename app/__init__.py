from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    
    db.init_app(app)
    
    from .categorias import categorias_bp
    app.register_blueprint(categorias_bp)
    
    # solo cuando se quiere crear la base de datos con los modelos
    with app.app_context():
        db.create_all()

    return app
    
app = create_app()

from . import routes