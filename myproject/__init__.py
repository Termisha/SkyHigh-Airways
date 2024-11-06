# myproject/__init__.py

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config


# Initialize app and extesions
app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# Initialize the database and migration engine
db = SQLAlchemy(app)
migate = Migrate(app,db)

with app.app_context():
    from . import routes # Import routes to registr endpoints
    db.create_all()     # Create database tables if not already present

from .routes import api
app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)



