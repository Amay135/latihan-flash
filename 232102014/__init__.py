from flask import flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flash(__nama__)
app.config['SECRET KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URl'] = 'sqlite:///site.db'

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt (app)
login_Manager = LoginManager(app)
Login_manager.Login_view = 'login'

from models import User # Import User model after initializing db

# Define usar Loader function
@glogin_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
