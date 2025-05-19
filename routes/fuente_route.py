from flask import Blueprint
from controllers.fuente_controller import (
    get_fuentes, get_fuente, create_fuente,
    update_fuente, delete_fuente
)

fuente_bp = Blueprint('fuente_bp', __name__)

@fuente_bp.route('/fuentes', methods=['GET'])
def route_get_fuentes():
    return get_fuentes()

@fuente_bp.route('/fuentes/<int:id>', methods=['GET'])
def route_get_fuente(id):
    return get_fuente(id)

@fuente_bp.route('/fuentes', methods=['POST'])
def route_create_fuente():
    return create_fuente()

@fuente_bp.route('/fuentes/<int:id>', methods=['PUT'])
def route_update_fuente(id):
    return update_fuente(id)

@fuente_bp.route('/fuentes/<int:id>', methods=['DELETE'])
def route_delete_fuente(id):
    return delete_fuente(id)