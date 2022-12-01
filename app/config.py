import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or '\x0b^\x96$#\xfe\x01\xa1\\q\xa8\xa7\x0b\xc5\x1a\x8b\xf2\xe1\x10g\x05\xec\xa7E'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')