from dotenv import load_dotenv;
from application.utils import get_env;

load_dotenv();

class Config:
    SECRET_KEY = get_env("SECRET");
    SQLALCHEMY_DATABASE_URI = get_env("DATABASE_URL");
    DEBUG = get_env("DEBUG")