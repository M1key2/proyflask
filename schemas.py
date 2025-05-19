from extensions import ma
from models.categoria_model import Categoria
from models.fuente_model import Fuente
from models.usuario_model import Usuario
from models.articulo_model import Articulo
from models.favorito_model import Favorito
from marshmallow import fields, validate



class UsuarioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Usuario
        ordered = True
    id = fields.Integer()
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=6))
    fecha_creacion = fields.DateTime(dump_only=True)

class CategoriaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Categoria
    id = fields.Integer()
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    descripcion = fields.String(validate=validate.Length(max=255))
    fecha_creacion = fields.DateTime(dump_only=True)

class FuenteSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Fuente

    id = fields.Integer()
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    descripcion = fields.String(validate=validate.Length(max=255))
    url = fields.URL(required=True)
    fecha_creacion = fields.DateTime()

class ArticuloSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Articulo

    id = fields.Integer()
    titulo = fields.String(required=True, validate=validate.Length(min=1, max=255))
    contenido = fields.String()
    id_categoria = fields.Integer(required=True)
    id_fuente = fields.Integer(required=True)
    fecha_publicacion = fields.DateTime(dump_only=True)


class FavoritoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Favorito

    id = fields.Integer()
    id_usuario = fields.Integer(required=True)
    id_articulo = fields.Integer(required=True)
    fecha_agregado = fields.DateTime()

# Inicializar schemas
usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)
categoria_schema = CategoriaSchema()
categorias_schema = CategoriaSchema(many=True)
fuente_schema = FuenteSchema()
fuentes_schema = FuenteSchema(many=True)
articulo_schema = ArticuloSchema()
articulos_schema = ArticuloSchema(many=True)
favorito_schema = FavoritoSchema()
favoritos_schema = FavoritoSchema(many=True) 