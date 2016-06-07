import os

# General Settings
basedir = os.path.abspath(os.path.dirname(__file__))
POSTS_PER_PAGE = 3  # Pagination



### Security Settings ###
# App Security
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# Open ID Provider settings
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
]


### Connection Settings ###
# SQLAlchemy Settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# Whoosh Alchemy settings
WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50

# Mail server settings
MAIL_SERVER = 'MAIL2.HOMEDEPOT.COM'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

ADMINS = ['carl_hillerman@homedepot.com']