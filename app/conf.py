import os

#creating base directory
basedir = os.path.abspath(os.path.dirname(__file__))


#configuring database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False


#flask_admin configuration
FLASK_ADMIN_SWATCH = 'cerulean'

#secret Key
SECRET_KEY = os.environ.get('SECRET_KEY')