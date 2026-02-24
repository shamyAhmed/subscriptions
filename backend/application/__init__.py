from flask import Flask, request;
from application.config import Config;
from application.extensions import register_db;
from application.utils import get_env, api_response;
from application.commands import register_commands;
from application.utils.logging_config import setup_logging;
from blueprints import register_blueprints;

def create_app(config=Config): 
    app = Flask(__name__);
    app.config.from_object(config);
    
    # register extensions
    register_db(app);
    register_commands(app);
    setup_logging(app);

    register_blueprints(app);

    def _is_auth_url(path):
        return path.startswith("/auth");

    @app.before_request
    def log_request():
        app.logger.info(
            "%s %s | remote_addr=%s | user_agent=%s",
            request.method,
            request.path,
            request.remote_addr or "-",
            request.user_agent.string if request.user_agent else "-",
        );
        if not _is_auth_url(request.path) and request.method in ("POST", "PUT", "PATCH"):
            body = request.get_data(as_text=True) or "-";
            app.logger.info("Request body: %s", body[:2000] if len(body) > 2000 else body);

    @app.errorhandler(404)
    def not_found(e):
        app.logger.warning("Not Found: %s", e);
        return api_response(error="Not Found", status_code=404, message="The requested resource was not found.");

    @app.errorhandler(500)
    def internal_error(e):
        app.logger.exception("Internal Server Error: %s", e);
        message = str(e) if app.debug else "An unexpected error occurred.";
        return api_response(error="Internal Server Error", status_code=500, message=message);

    @app.route("/")
    def hello_world():
        return "Hello test!!!!";
    
    return app;