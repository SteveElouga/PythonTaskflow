from .views import app
from . import models

from flask_migrate import Migrate

models.db.init_app(app)
migrate = Migrate(app, models.db)

# @app.before_request
def init_db():
    models.init_db()