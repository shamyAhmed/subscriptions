from flask import Flask;
from application.config import Config;
from application.extensions import register_db;
from models.utils.user_utils import create_single_user;

def create_app(config=Config): 
    app = Flask(__name__);
    app.config.from_object(config);
    
    # register extensions
    register_db(app);

    @app.route("/")
    def hello_world():
        return "Hello test!";

    @app.route("/create_user", methods=["POST"])
    def create_user():
        return "hello world!";
    
    return app;