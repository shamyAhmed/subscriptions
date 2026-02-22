from application.utils import get_env;
from application.extensions import db;
from models.user_models import User;
from datetime import date;

def create_single_user():
    user_name = get_env("USERNAME")
    password = get_env("PASSWORD")

    user = User(
        first_name="ahmed",
        last_name="elshamy",
        birth_date=date(2002, 11, 20),
        password=password,
        username = user_name
    );
    db.session.add(user);
    db.session.commit();