from application.extensions import db;
from sqlalchemy.orm import Mapped, mapped_column;
from datetime import date;
from models import BaseTimestamp;
from werkzeug.security import generate_password_hash, check_password_hash;
from application.utils import get_secret;

class User(db.Model, BaseTimestamp):
    __tablename__= "users";

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    birth_date: Mapped[date]
    username = Mapped[str]
    password_hash: Mapped[str] = mapped_column(init=False)

    def __init__(self, password, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.password = password;

    @property
    def password(self):
        return self.password_hash;

    @password.setter
    def password(self, value):
        secret = get_secret();
        self.password_hash = generate_password_hash(value + secret);
    
    def check_password(self, value):
        secret = get_secret();
        return check_password_hash(self.password_hash, value + secret);