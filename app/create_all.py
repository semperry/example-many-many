
from util.init_data import init_data


def create_all(app):
    with app.app_context():
        init_data()
