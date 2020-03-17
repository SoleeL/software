from app import db

class Categoria(db.Model):
    
    __tablename__ = "categoria"
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, unique=False, nullable=True)
    
    def __repr__(self):
        return f'==Categoria {self.nombre}=='
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    @staticmethod
    def obtener_por_id(id):
        return Categoria.query.get(id)
