from dotenv import load_dotenv;
import os;

load_dotenv();
env = lambda x: os.environ.get(x);

class Config:
    SECRET_KEY = env("SECRET");
    SQLALCHEMY_DATABASE_URI = env("DATABASE_URL");
    DEBUG = env("DEBUG")