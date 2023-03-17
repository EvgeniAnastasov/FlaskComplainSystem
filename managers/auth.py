from datetime import datetime, timedelta

import jwt
from decouple import config
from werkzeug.security import generate_password_hash

from app import db
from models.users import User


class AuthManager:
    @staticmethod
    def create_user(user_data):
        user_data["password"] = generate_password_hash(user_data["password"])
        user = User(**user_data)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def encode_token(user):
        payload = {"sub": user.id, "exp": datetime.utcnow() + timedelta(days=2)}
        return jwt.encode(payload, config("JWT_KEY"))
