from flask import current_app;

def get_secret():
    secret = current_app.config.get("SECRET_KEY");
    if secret is None:
        raise AttributeError("Secret is not defined in the application");
    return secret;