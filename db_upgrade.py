from migrate.versioning import api
from config import SQLALCHEMY_MIGRATE_REPO, SQLALCHEMY_DATABASE_URI

api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
v = api.version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print ('Current database version is ' + str(v))