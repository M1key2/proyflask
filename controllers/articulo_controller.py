from flask import request, jsonify
from models.articulo_model import db, Articulo
from extensions import ma
from schemas import (articulo_schema, articulos_schema,)


#get
def get_articulos():
    articulos = Articulo.query.all()
    return jsonify({"articulos": articulos_schema.dump(articulos)})

#getbyidd
def get_articulo(id):
    articulo = Articulo.query.get_or_404(id)
    return jsonify({"articulo": articulo_schema.dump(articulo)})

#post
def create_articulo():
    data = request.get_json()
    errors = articulo_schema.validate(data)
    if errors:
        return jsonify({"errors": errors}), 400
    nuevo_articulo = Articulo(**data)
    db.session.add(nuevo_articulo)
    db.session.commit()
    return jsonify({"articulo": articulo_schema.dump(nuevo_articulo)}), 201

#put
def update_articulo(id):
    articulo = Articulo.query.get_or_404(id)
    data = request.get_json()
    errors = articulo_schema.validate(data, partial=True)
    if errors:
        return jsonify({"errors": errors}), 400
    for key, value in data.items():
        setattr(articulo, key, value)
    db.session.commit()
    return jsonify({"articulo": articulo_schema.dump(articulo)})

def delete_articulo(id):
    articulo = Articulo.query.get_or_404(id)
    db.session.delete(articulo)
    db.session.commit()
    return jsonify({"message": "Artículo eliminado"})