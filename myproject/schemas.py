# myproject/schemas.py

from marshmallow import Schema, fields, validate, ValidationError

class UserSchema(Schema):
    first_name = fields.String(required=True, validate=validate.Length(min=2,max=30))
    last_name = fields.String(required=True, validate=validate.Length(min=2,max=30))
    date_of_birth = fields.Date(required=True)
    gender = fields.String(required=True, validate=validate.OneOf(["Male", "Female", "Other"]))
    email = fields.Email(required=True)
    phone_number = fields.String(required=True, validate=validate.Regexp(r"^\+?[1-9]\d{1,14}$"))

user_schema = UserSchema()