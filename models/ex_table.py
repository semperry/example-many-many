from app.db import db
import marshmallow as ma


class Ex(db.Model):
    __tablename__ = "exs"
    ex_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    users = db.relationship(
        "User", secondary="ex_association")  # <-
    journals = db.relationship("Journal")  # <-

    def __init__(self, name):
        self.name = name


class ExSchema(ma.Schema):
    class Meta:
        fields = ("ex_id", "name", 'journals')  # <-
    journals = ma.fields.Nested("JournalSchema", many=True)  # <-
    # users = ma.fields.Nested("UserSchema", only=[
    #                          'name', 'user_id'])


ex_schema = ExSchema()
exs_schema = ExSchema(many=True)
