from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from flask import Flask;
from flask_migrate import Migrate; 

class Base(DeclarativeBase, MappedAsDataclass):
    pass;

db = SQLAlchemy(model_class=Base);

def register_db(app: Flask):
    db.init_app(app);
    Migrate(app, db, command="migrate");