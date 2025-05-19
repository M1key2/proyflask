from flask import request
from models.categoria_model import db,  Categoria
from extensions import ma
from schemas import (categoria_schema, categorias_schema)


def get_categorias():
    categorias = Categoria.query.all()
    return {"categorias": categorias_schema.dump(categorias)}

def create_categoria():
    data = request.get_json()
    errors = categoria_schema.validate(data)
    if errors:
        return {"errors": errors}, 400
    nueva_categoria = Categoria(**data)
    db.session.add(nueva_categoria)
    db.session.commit()
    return {"categoria": categoria_schema.dump(nueva_categoria)}, 201

def get_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    return {"categoria": categoria_schema.dump(categoria)}

def update_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    data = request.get_json()
    errors = categoria_schema.validate(data, partial=True)
    if errors:
        return {"errors": errors}, 400
    for key, value in data.items():
        setattr(categoria, key, value)
    db.session.commit()
    return {"categoria": categoria_schema.dump(categoria)}

def delete_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    db.session.delete(categoria)
    db.session.commit()
    return {"message": "Categoría eliminada"}



