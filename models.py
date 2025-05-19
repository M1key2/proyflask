from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    favoritos = db.relationship('Favorito', backref='usuario', lazy=True)


class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255))
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    articulos = db.relationship('Articulo', backref='categoria', lazy=True)



class Fuente(db.Model):
    __tablename__ = 'fuentes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255))
    url = db.Column(db.String(255), nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    articulos = db.relationship('Articulo', backref='fuente', lazy=True)

class Articulo(db.Model):
    __tablename__ = 'articulos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(255), nullable=False)
    contenido = db.Column(db.Text)
    id_categoria = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    id_fuente = db.Column(db.Integer, db.ForeignKey('fuentes.id'), nullable=False)
    fecha_publicacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    favoritos = db.relationship('Favorito', backref='articulo', lazy=True)


class Favorito(db.Model):
    __tablename__ = 'favoritos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    id_articulo = db.Column(db.Integer, db.ForeignKey('articulos.id'), nullable=False)
    fecha_agregado = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 