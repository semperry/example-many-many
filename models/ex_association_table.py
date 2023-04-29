from app.db import db

# Finish this table


class ExAssociation(db.Model):
    __tablename__ = "ex_association"
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.user_id'), primary_key=True)
    ex_id = db.Column(db.Integer, db.ForeignKey('exs.ex_id'), primary_key=True)
