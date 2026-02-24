from flask import Flask


def register_blueprints(app: Flask):
    from auth_bp import auth_bp;
    app.register_blueprint(auth_bp);