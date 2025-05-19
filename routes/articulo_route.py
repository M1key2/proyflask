from flask import Blueprint
from controllers.articulo_controller import (
    get_articulos, get_articulo, create_articulo,
    update_articulo, delete_articulo
)

articulo_bp = Blueprint('articulo_bp', __name__)

@articulo_bp.route('/articulos', methods=['GET'])
def route_get_articulos():
    return get_articulos()

@articulo_bp.route('/articulos/<int:id>', methods=['GET'])
def route_get_articulo(id):
    return get_articulo(id)

@articulo_bp.route('/articulos', methods=['POST'])
def route_create_articulo():
    return create_articulo()

@articulo_bp.route('/articulos/<int:id>', methods=['PUT'])
def route_update_articulo(id):
    return update_articulo(id)

@articulo_bp.route('/articulos/<int:id>', methods=['DELETE'])
def route_delete_articulo(id):
    return delete_articulo(id)