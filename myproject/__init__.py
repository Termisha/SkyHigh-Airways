# myproject/__init__.py

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config


# Initialize app to Flask
app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
db = SQLAlchemy(app)

Migrate(app,db)

with app.app_context():
    from . import routes # Import routes to registr endpoints
    db.create_all()     # Create database tables if not already present

from .routes import api
app.register_blueprint(api, url_prefix='/api')



