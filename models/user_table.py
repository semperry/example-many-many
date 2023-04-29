from app.db import db
import marshmallow as ma


class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    exs = db.relationship("Ex", secondary="ex_association",
                          overlaps="users")  # <-

    def __init__(self, name):
        self.name = name


class UserSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "name", 'exs')  # <-
    exs = ma.fields.Nested("ExSchema", many=True, only=["name", "ex_id"])  # <-


user_schema = UserSchema()
users_schema = UserSchema(many=True)
