# from datetime import timedelta
import os
# import random
# import string

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'app.db')
JWT_SECRET_KEY = ">hi8uOzhk20/C'mX\x0c[]X9Vd:"
# JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)
# JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)