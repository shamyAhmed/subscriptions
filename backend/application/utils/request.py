from marshmallow import Schema;
from functools import wraps
from flask import request;
from application.utils.response import api_response;
from marshmallow import ValidationError

def validate_schema(schema: Schema, *args, **kwargs):
    def wrapper(fn):
        validation = schema(*args, **kwargs);
        @wraps(fn)
        def inner(*args, **kwargs):
            try:
                body = request.get_json(silent=True);
                if body is None:
                    return api_response(error="body must be json", status_code=400, message="body must be json");
                data = validation.load(body);
                return fn(*args, **kwargs, validated_data=data);
            except ValidationError as e:
                return api_response(error=e.messages, status_code=400, message="Validation Error Encountered");
        return inner;
    return wrapper;