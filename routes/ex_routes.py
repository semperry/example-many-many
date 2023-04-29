from flask import Blueprint, request
import controllers.ex_controller as ex

exs = Blueprint('exs', __name__)


@exs.route("/exs")
def get_exs():
    return ex.get_exs()


@exs.route("/ex/<id>")
def get_ex(id):
    return ex.get_ex(id)


@exs.route("/ex/<user_id>", methods=["POST"])
def add_ex(user_id):
    return ex.add_ex(request, user_id)
