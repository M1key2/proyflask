from flask import Blueprint
from controllers.categoria_controller import (
    get_categorias, get_categoria, create_categoria,
    update_categoria, delete_categoria
)

categoria_bp = Blueprint('categoria_bp', __name__)

@categoria_bp.route('/categorias', methods=['GET'])
def route_get_categorias():
    return get_categorias()

@categoria_bp.route('/categorias', methods=['POST'])
def route_create_categoria():
    return create_categoria()

@categoria_bp.route('/categorias/<int:id>', methods=['GET'])
def route_get_categoria(id):
    return get_categoria(id)

@categoria_bp.route('/categorias/<int:id>', methods=['PUT'])
def route_update_categoria(id):
    return update_categoria(id)

@categoria_bp.route('/categorias/<int:id>', methods=['DELETE'])
def route_delete_categoria(id):
    return delete_categoria(id)