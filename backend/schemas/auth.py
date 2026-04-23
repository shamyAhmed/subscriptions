from . import BaseSchema;
from marshmallow import fields, validates, ValidationError, validates_schema;

class LoginSchema(BaseSchema):
    username = fields.String(required=True)
    password = fields.String(load_only=True, required=True)

class RegisterSchema(LoginSchema):
    id = fields.Integer(dump_only=True)
    password_confirm = fields.String(load_only=True, required=True)
    birth_date = fields.Date(required=True);
    first_name = fields.String(required=True);
    last_name = fields.String(required=True);
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    @validates("password")
    def validate_password(self, value, data_key):
        errors = []
        if len(value) < 8:
            errors.append("password must be at least 8 characters")
        if not any(c.isupper() for c in value):
            errors.append("password must contain at least one uppercase letter")
        if not any(c.islower() for c in value):
            errors.append("password must contain at least one lowercase letter")
        if not any(c.isdigit() for c in value):
            errors.append("password must contain at least one digit")
        if errors:
            raise ValidationError(errors)

    @validates("username")
    def minimum(self, value, data_key):
        if(not value or len(value) < 8):
            raise ValidationError("username must be at least 8 characters");

    @validates_schema
    def same_password(self, data, **kwargs):
        password, confirmation = data.get("password"), data.get("password_confirm")
        if password and confirmation and password != confirmation:
            errors = dict(
                password_confirm="password and password confirmation must match",
                password="password and password confirmation must match"
            )
            raise ValidationError(errors);