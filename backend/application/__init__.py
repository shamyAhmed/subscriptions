from flask import Flask;
from application.config import Config;
from application.extensions import register_db;

def create_app(config=Config): 
    app = Flask(__name__);
    app.config.from_object(config);
    
    # register extensions
    register_db(app);

    @app.route("/")
    def hello_world():
        return "Hello world!";
    
    return app;