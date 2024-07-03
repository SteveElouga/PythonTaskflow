from TaskFlow import app
from TaskFlow import models

if __name__ == "__main__":
    with app.app_context():
        models.init_db()
    app.run(debug=True)