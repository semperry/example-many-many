from flask import Blueprint, request
import controllers.journal_controller as jc

journals = Blueprint("journals", __name__)


@journals.route("/journals")
def get_journals():
    return jc.get_journals()


@journals.route("/journal/<id>")
def get_journal(id):
    return jc.get_journal(id)


@journals.route("/journal/<ex_id>", methods=["POST"])
def add_journal(ex_id):
    return jc.add_journal(request, ex_id)
