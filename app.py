import os
from environs import Env

from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow

import routes
from app.db import init_db, db
from app.create_all import create_all


def create_app():
    app = Flask(__name__)
    env = Env()
    env.read_env()

    basedir = os.path.abspath(os.path.dirname(__file__))
    DATABASE_URL = "sqlite:///" + os.path.join(basedir, "app.sqlite")

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    init_db(app, db)

    app.register_blueprint(routes.exs)
    app.register_blueprint(routes.users)
    app.register_blueprint(routes.journals)

    return app


app = create_app()
CORS(app)
ma = Marshmallow(app)


if __name__ == "__main__":
    create_all(app)
    app.run(debug=True)
