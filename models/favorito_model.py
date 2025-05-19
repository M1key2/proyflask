from datetime import datetime
from extensions import db

class Favorito(db.Model):   
    __tablename__ = 'favoritos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    id_articulo = db.Column(db.Integer, db.ForeignKey('articulos.id'), nullable=False)
    fecha_agregado = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 