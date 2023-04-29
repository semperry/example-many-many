from app.db import db
import marshmallow as ma

# Similar to your card table


class Journal(db.Model):
    __tablename__ = "journals"
    journal_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(100), nullable=False)
    ex_id = db.Column(db.Integer, db.ForeignKey(
        "exs.ex_id"), nullable=True)  # <-

    def __init__(self, title, content, ex_id=None):  # <-
        self.title = title
        self.content = content
        self.ex_id = ex_id


class JournalSchema(ma.Schema):
    class Meta:
        fields = ("journal_id", "title", "content", "ex_id")  # <-
    # ex = ma.fields.Nested("ExSchema", exclude=["users"])


journal_schema = JournalSchema()
journals_schema = JournalSchema(many=True)
