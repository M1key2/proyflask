from flask import Blueprint
from controllers.usuario_controller import (
    get_usuarios, get_usuario, create_usuario,
    update_usuario, delete_usuario
)

usuario_bp = Blueprint('usuario_bp', __name__)

@usuario_bp.route('/usuarios', methods=['GET'])
def route_get_usuarios():
    return get_usuarios()

@usuario_bp.route('/usuarios/<int:id>', methods=['GET'])
def route_get_usuario(id):
    return get_usuario(id)

@usuario_bp.route('/usuarios', methods=['POST'])
def route_create_usuario():
    return create_usuario()

@usuario_bp.route('/usuarios/<int:id>', methods=['PUT'])
def route_update_usuario(id):
    return update_usuario(id)

@usuario_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def route_delete_usuario(id):
    return delete_usuario(id)