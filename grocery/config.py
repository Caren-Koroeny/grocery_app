from dotenv import load_dotenv
import os

#load_dotenv reads key-value pairs from a .env file
load_dotenv()

class Config:

    SECRET_KEY = os.getenv('SECRET_KEY')
    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    
    # Google Login
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
    GOOGLE_DISCOVERY_URL = os.getenv('GOOGLE_DISCOVERY_URL')
    
    # database
    SQLALCHEMY_DATABASE_URI =  os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
   