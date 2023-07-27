from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dash_app import create_dash_app
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_url_path='/static')

app.config['SECRET_KEY'] = os.getenv('flask_key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estoque.db'

db = SQLAlchemy(app)
dash_app = create_dash_app(app)

from siteportfolio import routes
