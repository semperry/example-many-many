from flask import jsonify
from app.db import db
from models.journal_table import Journal, journal_schema, journals_schema


def get_journals():
    journals = db.session.query(Journal).all()

    return jsonify(journals_schema.dump(journals))


def get_journal(id):
    journal = db.session.get(Journal, id)

    return jsonify(journal_schema.dump(journal))


def add_journal(request, ex_id):
    post_data = request.get_json()

    title = post_data.get("title")
    content = post_data.get("content")

    new_journal = Journal(title, content, ex_id)

    db.session.add(new_journal)
    db.session.commit()

    return jsonify(journal_schema.dump(new_journal))
