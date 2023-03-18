from datetime import datetime, timedelta

import jwt
from decouple import config
from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from models.users import User


class AuthManager:
    @staticmethod
    def create_user(user_data):
        user_data["password"] = generate_password_hash(user_data["password"])
        user = User(**user_data)
        db.session.add(user)
        # TODO handel db_session exception email already exist
        db.session.commit()
        return user

    @staticmethod
    def login_user(user_data):
        user = User.query.filter_by(email=user_data["email"]).first()
        if not user:
            raise BadRequest("Invalid email or password")

        if not check_password_hash(user.password, user_data["password"]):
            raise BadRequest("Invalid email or password")

        return user

    @staticmethod
    def encode_token(user):
        payload = {"sub": user.id, "exp": datetime.utcnow() + timedelta(days=2)}
        return jwt.encode(payload, config("JWT_KEY"))
