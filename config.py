import os
from sqlalchemy import create_engine
import urllib

class Config(object):
    SECRET_KEY='clave nueva'
    SESSION_COOKIE_SECRET=False
#datos para iniciar en nuestro msql 
class DevelomentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:messi1810@127.0.0.1/bdidgs801'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    