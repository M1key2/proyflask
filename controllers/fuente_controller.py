from flask import request
from models.fuente_model import db,  Fuente
from extensions import ma
from schemas import (fuente_schema, fuentes_schema)


def get_fuentes():
    fuentes = Fuente.query.all()
    return {"fuentes": fuentes_schema.dump(fuentes)}

def get_fuente(id):
    fuente = Fuente.query.get_or_404(id)
    return {"fuente": fuente_schema.dump(fuente)}

def create_fuente():
    data = request.get_json()
    errors = fuente_schema.validate(data)
    if errors:
        return {"errors": errors}, 400
    nueva_fuente = Fuente(**data)
    db.session.add(nueva_fuente)
    db.session.commit()
    return {"fuente": fuente_schema.dump(nueva_fuente)}, 201

def update_fuente(id):
    fuente = Fuente.query.get_or_404(id)
    data = request.get_json()
    errors = fuente_schema.validate(data, partial=True)
    if errors:
        return {"errors": errors}, 400
    for key, value in data.items():
        setattr(fuente, key, value)
    db.session.commit()
    return {"fuente": fuente_schema.dump(fuente)}

def delete_fuente(id):
    fuente = Fuente.query.get_or_404(id)
    db.session.delete(fuente)
    db.session.commit()
    return {"message": "Fuente eliminada"}



