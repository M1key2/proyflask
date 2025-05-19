from flask import request
from models.usuario_model import db,  Usuario
from extensions import ma
from schemas import (usuario_schema, usuarios_schema)


def get_usuarios():
    usuarios = Usuario.query.all()
    return {"usuarios": usuarios_schema.dump(usuarios)}

def get_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    return {"usuario": usuario_schema.dump(usuario)}

def create_usuario():
    data = request.get_json()
    errors = usuario_schema.validate(data)
    if errors:
        return {"errors": errors}, 400
    nuevo_usuario = Usuario(**data)
    db.session.add(nuevo_usuario)
    db.session.commit()
    return {"usuario": usuario_schema.dump(nuevo_usuario)}, 201

def update_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    data = request.get_json()
    errors = usuario_schema.validate(data, partial=True)
    if errors:
        return {"errors": errors}, 400
    for key, value in data.items():
        setattr(usuario, key, value)
    db.session.commit()
    return {"usuario": usuario_schema.dump(usuario)}

def delete_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return {"message": "Usuario eliminado"}

