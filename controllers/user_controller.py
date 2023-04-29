from flask import jsonify
from app.db import db
from models.user_table import User, user_schema, users_schema


def get_users():
    users = db.session.query(User).all()

    return jsonify(users_schema.dump(users))


def get_user(id):
    user = db.session.get(User, id)

    return jsonify(user_schema.dump(user))
