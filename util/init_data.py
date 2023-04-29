from app.db import db
from models.ex_association_table import ExAssociation
from models.user_table import User
from models.journal_table import Journal
from models.ex_table import Ex


def init_data():
    print("....Initializing Database....")
    db.drop_all()
    db.create_all()

    print("....Creating Mock Data....")
    user_one = User("crystal")
    user_two = User("ryan")
    ex_one = Ex("bart")
    ex_two = Ex("janie")

    db.session.add(user_one)
    db.session.add(user_two)
    db.session.add(ex_one)
    db.session.add(ex_two)
    db.session.flush()

    journal_one = Journal(
        "I can't go on.", "This dude is uber bad", ex_one.ex_id)
    journal_two = Journal(
        "Get rekt", "Can't believe this!", ex_one.ex_id)
    journal_three = Journal(
        "I'm aight", "Can't really complain", ex_two.ex_id)
    journal_four = Journal(
        "UGH", "Oh MAN I can't stand this person", ex_two.ex_id)

    db.session.add(journal_one)
    db.session.add(journal_two)
    db.session.add(journal_three)
    db.session.add(journal_four)

    user_one.exs.append(ex_one)
    user_two.exs.append(ex_one)
    user_two.exs.append(ex_two)

    print("....Saving Data....")
    db.session.commit()

    print("Seed Data Added")
