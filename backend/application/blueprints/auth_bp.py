from flask import Blueprint
from application.utils.request import validate_schema;
from application.utils.response import api_response;
from schemas.auth import RegisterSchema;
from sqlalchemy import select, literal, exists;
from models.user_models import User;
from application.extensions import db;

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@validate_schema(RegisterSchema)
def register(validated_data):
    # Check if there is a user with the same username;
    statement = select(exists(literal("1")).where(User.username == validated_data["username"]));
    user_exists = db.session.execute(statement).scalar();
    if user_exists:
        return api_response(error="user with this username already exists", status_code=400, message="User already exists");
    del validated_data["password_confirm"];

    user_data = {
        k: v for k, v in validated_data.items()
        if k != "password_confirm"
    }

    user = User(**user_data);

    db.session.add(user);
    db.session.commit();
    user_schema = RegisterSchema()
    user = user_schema.dump(user);

    return api_response(user, status_code=201, message="User created successfully");

    
auth_bp.add_url_rule("/register", "register", register, methods=["POST"])