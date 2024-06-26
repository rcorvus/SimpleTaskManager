from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
from dotenv import dotenv_values
config = dotenv_values(".env")
app.config['SECRET_KEY'] = config["SECRET_KEY"]
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)