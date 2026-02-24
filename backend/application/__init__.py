from flask import Flask;
from application.config import Config;
from application.extensions import register_db;
from application.utils import get_env
from application.commands import register_commands;
from blueprints import register_blueprints;

def create_app(config=Config): 
    app = Flask(__name__);
    app.config.from_object(config);
    
    # register extensions
    register_db(app);
    register_commands(app);

    register_blueprints(app);

    @app.route("/")
    def hello_world():
        return "Hello test!!!!";
    
    return app;