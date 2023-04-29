from flask import jsonify
from app.db import db
from models.ex_table import Ex, ex_schema, exs_schema
from models.user_table import User, user_schema


def get_exs():
    exs = db.session.query(Ex).all()

    return jsonify(exs_schema.dump(exs))


def get_ex(id):
    ex = db.session.get(Ex, id)

    return jsonify(ex_schema.dump(ex))


'''
You must create an ex,
query for the user they belong to (yourself, try just using auth_info),
append the created ex to the user exs list
db commit
'''


def add_ex(request, user_id):
    post_data = request.get_json()
    name = post_data.get("name")

    new_ex = Ex(name)
    user = db.session.get(User, int(user_id))

    db.session.flush()  # <- this will serialize data without writing to the db

    user.exs.append(new_ex)
    db.session.commit()

    ex = db.session.get(Ex, new_ex.ex_id)

    return jsonify(ex_schema.dump(ex))
