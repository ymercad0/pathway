import os
SECRET_KEY = os.urandom(16).hex()
MONGO_DBNAME = os.environ.get('MONGO_DBNAME')
MONGO_URI = os.environ.get('MONGO_URI')