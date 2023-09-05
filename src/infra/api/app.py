from flask import Flask
from src.infra.api.routes import api_blueprint
app = Flask(__name__)

app.register_blueprint(api_blueprint, url_prefix='/api')
