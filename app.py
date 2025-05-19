from flask import Flask, request
from models import db, Usuario, Categoria, Fuente, Articulo, Favorito
from extensions import ma  
from schemas import (
    usuario_schema, usuarios_schema,
    categoria_schema, categorias_schema,
    fuente_schema, fuentes_schema,
    articulo_schema, articulos_schema,
    favorito_schema, favoritos_schema
)



# Inicialización de la aplicación
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///noticias.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de extensiones
db.init_app(app)


# Crear todas las tablas
with app.app_context():
    db.create_all()

# Ruta de inicio
@app.route('/')
def hello_world():
   
    return '¡Hola, mundo! Esta es la API de Noticias.'

@app.route('/articulos', methods=['GET'])
def get_articulos():
    articulos = Articulo.query.all()
    return {"articulos": articulos_schema.dump(articulos)}

@app.route('/articulos/<int:id>', methods=['GET'])
def get_articulo(id):
    articulo = Articulo.query.get_or_404(id)
    return {"articulos": articulo_schema.dump(articulo)}

@app.route('/articulos', methods=['POST'])
def create_articulo():
    data = request.get_json()
    errors = articulo_schema.validate(data)
    if errors:
        return {"errors": errors}, 400
    nuevo_articulo = Articulo(**data)
    db.session.add(nuevo_articulo)
    db.session.commit()
    return {"articulo": articulo_schema.dump(nuevo_articulo)}, 201

@app.route('/articulos/<int:id>', methods=['PUT'])
def update_articulo(id):
    articulo = Articulo.query.get_or_404(id)
    data = request.get_json()
    errors = articulo_schema.validate(data, partial=True)
    if errors:
        return {"errors": errors}, 400
    for key, value in data.items():
        setattr(articulo, key, value)
    db.session.commit()
    return {"articulo": articulo_schema.dump(articulo)}

@app.route('/articulos/<int:id>', methods=['DELETE'])
def delete_articulo(id):
    articulo = Articulo.query.get_or_404(id)
    db.session.delete(articulo)
    db.session.commit()
    return {"message": "Artículo eliminado"}

# --- CRUD para Categorías ---
@app.route('/categorias', methods=['GET'])
def get_categorias():
    categorias = Categoria.query.all()
    return {"categorias": categorias_schema.dump(categorias)}

@app.route('/categorias', methods=['POST'])
def create_categoria():
    data = request.get_json()
    errors = categoria_schema.validate(data)
    if errors:
        return {"errors": errors}, 400
    nueva_categoria = Categoria(**data)
    db.session.add(nueva_categoria)
    db.session.commit()
    return {"categoria": categoria_schema.dump(nueva_categoria)}, 201

@app.route('/categorias/<int:id>', methods=['GET'])
def get_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    return {"categoria": categoria_schema.dump(categoria)}

@app.route('/categorias/<int:id>', methods=['PUT'])
def update_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    data = request.get_json()
    errors = categoria_schema.validate(data, partial=True)
    if errors:
        return {"errors": errors}, 400
    for key, value in data.items():
        setattr(categoria, key, value)
    db.session.commit()
    return {"categoria": categoria_schema.dump(categoria)}

@app.route('/categorias/<int:id>', methods=['DELETE'])
def delete_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    db.session.delete(categoria)
    db.session.commit()
    return {"message": "Categoría eliminada"}

# --- CRUD para Usuarios ---
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return {"usuarios": usuarios_schema.dump(usuarios)}

@app.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    return {"usuario": usuario_schema.dump(usuario)}
@app.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.get_json()
    errors = usuario_schema.validate(data)
    if errors:
        return {"errors": errors}, 400
    nuevo_usuario = Usuario(**data)
    db.session.add(nuevo_usuario)
    db.session.commit()
    return {"usuario": usuario_schema.dump(nuevo_usuario)}, 201

@app.route('/usuarios/<int:id>', methods=['PUT'])
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

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return {"message": "Usuario eliminado"}

# --- CRUD para Fuentes ---
@app.route('/fuentes', methods=['GET'])
def get_fuentes():
    fuentes = Fuente.query.all()
    return {"fuentes": fuentes_schema.dump(fuentes)}

@app.route('/fuentes/<int:id>', methods=['GET'])
def get_fuente(id):
    fuente = Fuente.query.get_or_404(id)
    return {"fuente": fuente_schema.dump(fuente)}

@app.route('/fuentes', methods=['POST'])
def create_fuente():
    data = request.get_json()
    errors = fuente_schema.validate(data)
    if errors:
        return {"errors": errors}, 400
    nueva_fuente = Fuente(**data)
    db.session.add(nueva_fuente)
    db.session.commit()
    return {"fuente": fuente_schema.dump(nueva_fuente)}, 201

@app.route('/fuentes/<int:id>', methods=['PUT'])
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

@app.route('/fuentes/<int:id>', methods=['DELETE'])
def delete_fuente(id):
    fuente = Fuente.query.get_or_404(id)
    db.session.delete(fuente)
    db.session.commit()
    return {"message": "Fuente eliminada"}

# --- CRUD para Favoritos ---
@app.route('/favoritos', methods=['GET'])
def get_favoritos():
    favoritos = Favorito.query.all()
    return {"favoritos": favoritos_schema.dump(favoritos)}

@app.route('/favoritos/<int:id>', methods=['GET'])
def get_favorito(id):
    favorito = Favorito.query.get_or_404(id)
    return {"favorito": favorito_schema.dump(favorito)}

@app.route('/favoritos', methods=['POST'])
def create_favorito():
    data = request.get_json()
    errors = favorito_schema.validate(data)
    if errors:
        return {"errors": errors}, 400
    nuevo_favorito = Favorito(**data)
    db.session.add(nuevo_favorito)
    db.session.commit()
    return {"favorito": favorito_schema.dump(nuevo_favorito)}, 201

@app.route('/favoritos/<int:id>', methods=['PUT'])
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

@app.route('/favoritos/<int:id>', methods=['DELETE'])
def delete_favorito(id):
    favorito = Favorito.query.get_or_404(id)
    db.session.delete(favorito)
    db.session.commit()
    return {"message": "Favorito eliminado"}

if __name__ == '__main__':
    app.run(debug=True) 