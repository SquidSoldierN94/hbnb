from flask import Flask
from app.api.endpoints import api_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_bp, url_prefix='/api')
    return app
