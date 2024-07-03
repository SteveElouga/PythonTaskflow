from datetime import datetime
import logging as lg
import os

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    short_description = db.Column(db.String(200), nullable = False)
    created_at = db.Column(db.DateTime, nullable = False, default = datetime.now)
    updated_at = db.Column(db.DateTime, nullable = False, default = datetime.now, onupdate = datetime.utcnow)
    
    def __init__(self, name, description):
        self.name = name
        self.short_description = description
        
        
def init_db():
    if not os.path.exists("app.db"):       
        db.drop_all()
        db.create_all()
        lg.warning('Database initialized!')
            
    else:
        lg.warning("Database is already initialized!")