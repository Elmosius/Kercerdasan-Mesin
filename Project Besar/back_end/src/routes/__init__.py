from flask import Flask
from controllers.predict_controller import predict_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(predict_bp, url_prefix='/')
    return app

app = create_app()
