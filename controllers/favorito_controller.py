from flask import request
from models.favorito_model import db,  Favorito
from extensions import ma
from schemas import (favorito_schema, favoritos_schema,)


def get_favoritos():
    favoritos = Favorito.query.all()
    return {"favoritos": favoritos_schema.dump(favoritos)}

def get_favorito(id):
    favorito = Favorito.query.get_or_404(id)
    return {"favorito": favorito_schema.dump(favorito)}

def create_favorito():
    data = request.get_json()
    errors = favorito_schema.validate(data)
    if errors:
        return {"errors": errors}, 400
    nuevo_favorito = Favorito(**data)
    db.session.add(nuevo_favorito)
    db.session.commit()
    return {"favorito": favorito_schema.dump(nuevo_favorito)}, 201

def update_favorito(id):
    favorito = Favorito.query.get_or_404(id)
    data = request.get_json()
    errors = favorito_schema.validate(data, partial=True)
    if errors:
        return {"errors": errors}, 400
    for key, value in data.items():
        setattr(favorito, key, value)
    db.session.commit()
    return {"favorito": favorito_schema.dump(favorito)}


def delete_favorito(id):
    favorito = Favorito.query.get_or_404(id)
    db.session.delete(favorito)
    db.session.commit()
    return {"message": "Favorito eliminado"}