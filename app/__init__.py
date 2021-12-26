from flask import Flask, request

app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy


app.config["SECRET_KEY"] = "015c070a0545147a8c5d7ceffded731f"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///student.db"

db = SQLAlchemy(app)

from app import routes