from extensions import ma
from marshmallow import fields, validate

class UsuarioSchema(ma.Schema):
    class Meta:
        ordered = True
    id = fields.Integer()
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=6))
    fecha_creacion = fields.DateTime(dump_only=True)

class CategoriaSchema(ma.Schema):
    class Meta:
        ordered = True
    id = fields.Integer()
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    descripcion = fields.String(validate=validate.Length(max=255))
    fecha_creacion = fields.DateTime(dump_only=True)

class FuenteSchema(ma.Schema):
    class Meta:
        ordered = True
    id = fields.Integer()
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    descripcion = fields.String(validate=validate.Length(max=255))
    url = fields.URL(required=True)
    fecha_creacion = fields.DateTime()

class ArticuloSchema(ma.Schema):
    class Meta:
        ordered = True
    id = fields.Integer()
    titulo = fields.String(required=True, validate=validate.Length(min=1, max=255))
    contenido = fields.String()
    id_categoria = fields.Integer(required=True)
    id_fuente = fields.Integer(required=True)
    fecha_publicacion = fields.DateTime(dump_only=True)


class FavoritoSchema(ma.Schema):
    class Meta:
        ordered = True
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