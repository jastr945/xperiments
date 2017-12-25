import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


# instantiate the db
db = SQLAlchemy()

UPLOAD_FOLDER = '/static/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def create_app():

    # instantiate the app
    app = Flask(__name__)

    # enable CORS
    CORS(app)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    # set up extensions
    db.init_app(app)

    # register blueprints
    from project.api.views import albums_blueprint
    app.register_blueprint(albums_blueprint)

    return app
