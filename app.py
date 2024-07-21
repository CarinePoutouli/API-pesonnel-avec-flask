from flask import Flask

from extensions import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv
from flask_cors import CORS

from personne.vues.vues import personne

app = Flask(__name__)

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

cors = CORS()

# Maintenant vous pouvez accéder aux variables d'environnement
flask_app = os.getenv('FLASK_APP')
flask_env = os.getenv('FLASK_ENV')
database_url = os.getenv('DATABASE_URL')
secret_key = os.getenv('SECRET_KEY')
#
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = secret_key
app.config['JWT_SECRET_KEY'] = secret_key
app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json", "query_string"]


app.register_blueprint(personne, url_prefix='/personne/')

cors.init_app(
    app,
    resources={r"*": {"origins": "*"}}
)
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

from personne.model.model import Utilisateur   # noqa: F401

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8080,
        debug=True
    )
