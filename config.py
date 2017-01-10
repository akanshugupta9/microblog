import os

WTF_CSRF_ENABLE = True
SECRET_KEY = 'Akanshu-Gupta'

OPENID_PROVIDERS = [
    { 'name' : 'Google', 'url' : 'https://www.google.com/accounts/o8/id'},
    { 'name' : 'Yahoo', 'url' : 'https://me.yahoo.com'},
    { 'name' : 'AOL', 'url' : 'http://openid.aol.com/<username>'},
    { 'name' : 'Flickr', 'url' : 'http://www.flickr.com/<username>'},
    { 'name' : 'MyOpenId', 'url' : 'https://www.myopenid.com'}
]

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join( basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join( basedir, 'db_repository')

MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

ADMINS = ['akg@something.com']