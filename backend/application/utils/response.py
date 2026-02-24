from flask import jsonify, make_response


def api_response(data=None, error=None, status_code=200, message=None):
    payload = {
        "data": data if error is None else None,
        "error": error,
        "message": message,
    };
    return make_response(jsonify(payload), status_code);
