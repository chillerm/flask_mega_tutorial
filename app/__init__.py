import os

# Configuration of main flask application
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

# Configuration of SQLAlchemy SQLite DB interface
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

# Configure Login Manager / Authentication
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))


# Configure Emails
from flask_mail import Mail
mail = Mail(app)


# Logging Setup
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD

if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    credentials = None
    if MAIL_USERNAME or MAIL_PASSWORD:
        credentials = (MAIL_USERNAME, MAIL_PASSWORD)
    mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT), 'no-reply@' + MAIL_SERVER, ADMINS, 'microblog failure'
                               , credentials)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler(basedir + '/tmp/microblog.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s: %(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('microblog startup')

# Configure date / timestamp handling
# This exposes the momentjs as a global variable
from .momentjs import momentjs
app.jinja_env.globals['momentjs'] = momentjs

# Multi Language support with Babel
from flask_babel import Babel
babel = Babel(app)

from app import views, models