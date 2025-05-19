from flask import Flask
from extensions import db
from config import Config
from routes.articulo_route import articulo_bp
from routes.categoria_route import categoria_bp
from routes.fuente_route import fuente_bp
from routes.usuario_route import usuario_bp
from routes.favorito_route import favorito_bp



app = Flask(__name__)
app.config.from_object(Config)


app.register_blueprint(articulo_bp)
app.register_blueprint(categoria_bp)
app.register_blueprint(fuente_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(favorito_bp)

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def hello_world():
    return 'News api'







