from app import db
from flask_login import UserMixin


class Usuario(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, unique=False, nullable=False)
    correo = db.Column(db.String, unique=False, nullable=False)
    password = db.Column(db.String, unique=False, nullable=False)
    
    def __init__ (self,nombre,correo,password):
        self.nombre = nombre
        self.correo = correo
        self.password = hash(password)
        
    def __repr__(self):
        return f'<Usuario { self.nombre }>'

    def comprobar_password(self,password):
        return self.password == hash(password)
    
    def guardar(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def obtener_por_id(id):
        return Usuario.query.get(id)
    
    @staticmethod
    def obtener_por_correo(correo):
        return Usuario.query.filter_by(correo=correo).first()