from migrate.versioning import api
from config import SQLALCHEMY_MIGRATE_REPO, SQLALCHEMY_DATABASE_URI

v = api.version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, v-1)
v = api.version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print ('Current database version is ' + str(v))