from flask import jsonify, make_response, current_app, has_app_context


def api_response(data=None, error=None, status_code=200, message=None):
    payload = {
        "data": data if error is None else None,
        "error": error,
        "message": message,
    };
    if has_app_context():
        current_app.logger.info("Response %s: %s", status_code, payload);
    return make_response(jsonify(payload), status_code);
