from application.utils import get_env;
from application.extensions import db;
from models.user_models import User;
from datetime import date;
from sqlalchemy import select;

def create_single_user():
    user_name = get_env("USERNAME")
    password = get_env("PASSWORD")

    user = db.session.execute(select(User)).scalar_one_or_none();
    if user is None:
        user = User(
            first_name="ahmed",
            last_name="elshamy",
            birth_date=date(2002, 11, 20),
            password=password,
            username = user_name
        );
        db.session.add(user);
        db.session.commit();
        print("user created");
    else:
        print("user exists");