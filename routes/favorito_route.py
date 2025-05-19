from flask import Blueprint
from controllers.favorito_controller import (
    get_favoritos, get_favorito, create_favorito,
    update_favorito, delete_favorito
)

favorito_bp = Blueprint('favorito_bp', __name__)

@favorito_bp.route('/favoritos', methods=['GET'])
def route_get_favoritos():
    return get_favoritos()

@favorito_bp.route('/favoritos/<int:id>', methods=['GET'])
def route_get_favorito(id):
    return get_favorito(id)

@favorito_bp.route('/favoritos', methods=['POST'])
def route_create_favorito():
    return create_favorito()

@favorito_bp.route('/favoritos/<int:id>', methods=['PUT'])
def route_update_favorito(id):
    return update_favorito(id)

@favorito_bp.route('/favoritos/<int:id>', methods=['DELETE'])
def route_delete_favorito(id):
    return delete_favorito(id)