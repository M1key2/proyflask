from datetime import datetime
from extensions import db


class Fuente(db.Model):
    __tablename__ = 'fuentes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255))
    url = db.Column(db.String(255), nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    articulos = db.relationship('Articulo', backref='fuente', lazy=True)