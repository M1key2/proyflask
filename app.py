from flask import Flask, request
from extensions import ma, db


from controllers.articulo_controller import (
    get_articulos, get_articulo, create_articulo,
    update_articulo, delete_articulo
)
from controllers.categoria_controller import (
    get_categorias, create_categoria,
    get_categoria, update_categoria,
    delete_categoria
)
from controllers.usuario_controller import (
    get_usuarios, get_usuario, create_usuario, update_usuario, delete_usuario
)
from controllers.fuente_controller import (
    get_fuentes, get_fuente, create_fuente,
    update_fuente, delete_fuente
)
from controllers.favorito_controller import (
    get_favoritos, get_favorito, create_favorito,
    update_favorito, delete_favorito
)



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///noticias.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)



with app.app_context():
    db.create_all()


@app.route('/')
def hello_world():
   
    return '¡Hola, mundo! Esta es la API de Noticias.'

@app.route('/articulos', methods=['GET'])
def route_get_articulos():
    return get_articulos()


@app.route('/articulos/<int:id>', methods=['GET'])
def route_get_articulo(id):
    return get_articulo(id)


@app.route('/articulos', methods=['POST'])
def route_create_articulo():
    return create_articulo()


@app.route('/articulos/<int:id>', methods=['PUT'])
def route_update_articulo(id):
    return update_articulo(id)


@app.route('/articulos/<int:id>', methods=['DELETE'])
def route_delete_articulo(id):
    return delete_articulo(id)


@app.route('/categorias', methods=['GET'])
def route_get_categorias():
    return get_categorias()

@app.route('/categorias', methods=['POST'])
def route_create_categoria():
    return create_categoria()

@app.route('/categorias/<int:id>', methods=['GET'])
def route_get_categoria(id):
    return get_categoria(id)


@app.route('/categorias/<int:id>', methods=['PUT'])
def route_update_categoria(id):
    return update_categoria(id)

@app.route('/categorias/<int:id>', methods=['DELETE'])
def route_delete_categoria(id):
    return delete_categoria(id)


@app.route('/usuarios', methods=['GET'])
def route_get_usuarios():
    return get_usuarios()

@app.route('/usuarios/<int:id>', methods=['GET'])
def route_get_usuario(id):
    return get_usuario(id)

@app.route('/usuarios', methods=['POST'])
def route_create_usuario():
    return create_usuario()

@app.route('/usuarios/<int:id>', methods=['PUT'])
def route_update_usuario(id):
    return update_usuario(id)


@app.route('/usuarios/<int:id>', methods=['DELETE'])
def route_delete_usuario(id):
    return delete_usuario(id)



@app.route('/fuentes', methods=['GET'])
def route_get_fuentes():
    return get_fuentes()

@app.route('/fuentes/<int:id>', methods=['GET'])
def route_get_fuente(id):
    return get_fuente(id)

@app.route('/fuentes', methods=['POST'])
def route_create_fuente():
    return create_fuente()


@app.route('/fuentes/<int:id>', methods=['PUT'])
def route_update_fuente(id):
    return update_fuente(id)


@app.route('/fuentes/<int:id>', methods=['DELETE'])
def route_delete_fuente(id):
    return delete_fuente(id)


@app.route('/favoritos', methods=['GET'])
def route_get_favoritos():
    return get_favoritos()


@app.route('/favoritos/<int:id>', methods=['GET'])
def route_get_favorito(id):
    return get_favorito(id)


@app.route('/favoritos', methods=['POST'])
def route_create_favorito():
    return create_favorito()

@app.route('/favoritos/<int:id>', methods=['PUT'])
def route_update_favorito(id):
    return update_favorito(id)

@app.route('/favoritos/<int:id>', methods=['DELETE'])
def route_delete_favorito(id):
    return delete_favorito(id)




