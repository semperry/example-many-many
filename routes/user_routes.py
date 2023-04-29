from flask import Blueprint
import controllers.user_controller as u

users = Blueprint("users", __name__)


@users.route("/users")
def get_users():
    return u.get_users()


@users.route("/user/<id>")
def get_user(id):
    return u.get_user(id)
