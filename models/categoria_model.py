from datetime import datetime
from extensions import db 



class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255))
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    articulos = db.relationship('Articulo', backref='categoria', lazy=True)
